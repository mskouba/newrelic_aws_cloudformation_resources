import logging
from typing import Any, MutableMapping, Optional
from unicodedata import name

from cloudformation_cli_python_lib import (
    Action,
    HandlerErrorCode,
    OperationStatus,
    ProgressEvent,
    Resource,
    SessionProxy,
    exceptions,
    identifier_utils,
)

from .models import ResourceHandlerRequest, ResourceModel, _Nrql, _Expiration, _Signal, _Term
from cloudformation_cli_python_lib.utils import deserialize_list


from .newrelic_api_client import NewRelicApiRequest
from dataclasses import fields

import os


LOG = logging.getLogger(__name__)
TYPE_NAME = "NewRelic::Alerts::Condition"

resource = Resource(TYPE_NAME, ResourceModel)
test_entrypoint = resource.test_entrypoint


@resource.handler(Action.CREATE)
def create_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )

    LOG.info("Beginning create handler for {}: {}".format(TYPE_NAME, model.Condition.Name))

    try:
        
        # Prepare request params for create call
        params = {
            "accountId": model.AccountId,
            "policyId": model.Condition.PolicyId,
            "name": model.Condition.Name,
            "enabled": model.Condition.Enabled,
            "violationTimeLimitSeconds": model.Condition.ViolationTimeLimitSeconds,
            "nrqlInput":{field.name[0].lower() + field.name[1:]: getattr(model.Condition.Nrql, field.name) for field in fields(model.Condition.Nrql)},
            "expirationInput": {field.name[0].lower() + field.name[1:]: getattr(model.Condition.Expiration, field.name) for field in fields(model.Condition.Expiration)},
            "signalInput": {field.name[0].lower() + field.name[1:]: getattr(model.Condition.Signal, field.name) for field in fields(model.Condition.Signal)if getattr(model.Condition.Signal, field.name) is not None},
            "termsInput": [{field.name[0].lower() + field.name[1:]:getattr(x, field.name) for field in fields(x) if getattr(x, field.name) is not None} for x in model.Condition.Terms]
            }
        
        # Static and baseline conditions use different API functions and thus need to be handled by separate queries
        if model.Condition.Type == "STATIC":
            result = NewRelicApiRequest(key=model.ApiKey, template=os.path.abspath(os.getcwd()) + "/newrelic_alerts_condition/queries/ConditionStaticCreate.gql", params=params)
            model.Condition.Id = int(result['alertsNrqlConditionStaticCreate']['id'])
            LOG.info("Successfully created condition {}".format(model.Condition.Id))

            return ProgressEvent(status=OperationStatus.SUCCESS, resourceModel=model)
            
        elif model.Condition.Type == "BASELINE":
            # Add baseline specific param to parameters
            params["baselineDirection"] = model.Condition.BaselineDirection
            result = NewRelicApiRequest(key=model.ApiKey, template=os.path.abspath(os.getcwd()) + "/newrelic_alerts_condition/queries/ConditionBaselineCreate.gql", params=params)
            model.Condition.Id = result['alertsNrqlConditionBaselineCreate']['id']
            LOG.info("Successfully created condition {}".format(model.Condition.Id))
            
            return ProgressEvent(status=OperationStatus.SUCCESS, resourceModel=model)
            
    except:
        raise        

    
@resource.handler(Action.UPDATE)
def update_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )

    LOG.info("Beginning update handler for {}: {}".format(TYPE_NAME, model.Condition.Name))

    try:

        # Returns a not found error if the condition Id passed to update is none
        if model.Condition.Id == None:
            raise exceptions.NotFound("Condition ID", model.Condition.Id)

        if model.Condition.PolicyId != request.previousResourceState.Condition.PolicyId:
            raise exceptions.NotUpdatable("Changing policy ID requires create and delete actions rather than update.")

        if model.Condition.Type != request.previousResourceState.Condition.Type:
            raise exceptions.NotUpdatable("Changing condition type requires create and delete actions rather than update.")
            
        else:

            # Prepare request params for update call
            params = {
                "accountId": model.AccountId,
                "id": model.Condition.Id,
                "name": model.Condition.Name,
                "enabled": model.Condition.Enabled,
                "violationTimeLimitSeconds": model.Condition.ViolationTimeLimitSeconds,
                "nrqlInput":{field.name[0].lower() + field.name[1:]: getattr(model.Condition.Nrql, field.name) for field in fields(model.Condition.Nrql)},
                "expirationInput": {field.name[0].lower() + field.name[1:]: getattr(model.Condition.Expiration, field.name) for field in fields(model.Condition.Expiration) if getattr(model.Condition.Expiration, field.name) is not None},
                "signalInput": {field.name[0].lower() + field.name[1:]: getattr(model.Condition.Signal, field.name) for field in fields(model.Condition.Signal)if getattr(model.Condition.Signal, field.name) is not None},
                "termsInput": [{field.name[0].lower() + field.name[1:]:getattr(x, field.name) for field in fields(x) if getattr(x, field.name) is not None} for x in model.Condition.Terms]
                }

            # Static and baseline conditions use different API functions and thus need to be handled by separate queries
            if model.Condition.Type == "STATIC":
                result = NewRelicApiRequest(key=model.ApiKey, template=os.path.abspath(os.getcwd()) + "/newrelic_alerts_condition/queries/ConditionStaticUpdate.gql", params=params)
                model.Condition.Id = int(result['alertsNrqlConditionStaticUpdate']['id'])
                LOG.info("Successfully updated condition {}".format(model.Condition.Id))

                return ProgressEvent(status=OperationStatus.SUCCESS, resourceModel=model)
            
            elif model.Condition.Type == "BASELINE":
                params["baselineDirection"] = model.Condition.BaselineDirection
                result = NewRelicApiRequest(key=model.ApiKey, template=os.path.abspath(os.getcwd()) + "/newrelic_alerts_condition/queries/ConditionBaselineUpdate.gql", params=params)
                model.Condition.Id = int(result['alertsNrqlConditionBaselineUpdate']['id'])
                LOG.info("Successfully updated condition {}".format(model.Condition.Id))

                return ProgressEvent(status=OperationStatus.SUCCESS, resourceModel=model)
                
    except: 
        raise


@resource.handler(Action.DELETE)
def delete_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=None,
    )
    
    LOG.info("Beginning delete handler for {}: {}".format(TYPE_NAME, model.Condition.Name))

    try:
        
        #Call New Relic API to delete condition
        params = {"accountId": model.AccountId, "id": model.Condition.Id}
        result = NewRelicApiRequest(key=model.ApiKey, template=os.path.abspath(os.getcwd()) + "/newrelic_alerts_condition/queries/ConditionDelete.gql", params=params)

        LOG.info("Successfully deleted condition {}".format(result["alertsConditionDelete"]["id"]))

        return ProgressEvent(status=OperationStatus.SUCCESS)

    except:
        raise 


@resource.handler(Action.READ)
def read_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    
    LOG.info("Beginning read handler for {}: {}".format(TYPE_NAME, model.Condition.Name))
 
    try: 

        # Call New Relic API and return payload as result, then get just the relevant info as condition for readability
        params = {"accountId": model.AccountId, "id": model.Condition.Id}
        result = NewRelicApiRequest(key=model.ApiKey, template=os.path.abspath(os.getcwd()) + "/newrelic_alerts_condition/queries/ConditionRead.gql", params=params)
        condition = result["actor"]["account"]["alerts"]["nrqlCondition"]
        
        # Write payload data to model
        model.Condition.Name = condition["name"]
        model.Condition.Id = int(condition["id"])
        model.Condition.Enabled = condition["enabled"]
        model.Condition.Description = condition["description"]
        model.Condition.PolicyId = int(condition["policyId"])
        model.Condition.RunbookUrl = condition["runbookUrl"]
        model.Condition.Type = condition["type"]
        model.Condition.ViolationTimeLimitSeconds = condition["violationTimeLimitSeconds"]
        model.Condition.Nrql = _Nrql._deserialize({key[0].upper() + key[1:]: value for key, value in condition["nrql"].items()})
        model.Condition.Expiration = _Expiration._deserialize({key[0].upper() + key[1:]: value for key, value in condition["expiration"].items() if value is not None})
        model.Condition.Signal = _Signal._deserialize({key[0].upper() + key[1:]: value for key, value in condition["signal"].items() if value is not None})
        model.Condition.Terms = deserialize_list([{key[0].upper() + key[1:]:value for key, value in x.items() if value is not None} for x in condition["terms"]], _Term)

        LOG.info("Completed read handler for {}: {}".format(TYPE_NAME, model.Condition.Name))

        return ProgressEvent(
            status=OperationStatus.SUCCESS,
            resourceModel=model,
        )

    except:
        raise 


