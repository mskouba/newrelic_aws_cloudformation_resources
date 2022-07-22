import logging
from typing import Any, MutableMapping, Optional

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

from .models import ResourceHandlerRequest, ResourceModel

from .newrelic_api_client import NewRelicApiRequest

import os

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)

TYPE_NAME = "NewRelic::Alerts::Policy"

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


    try:

        LOG.info("Beginning create handler for {}: {}".format(TYPE_NAME, model.Policy.Name))
        
        params = {"accountId": model.AccountId, "alertsPolicyInput": {"name": model.Policy.Name, "incidentPreference": model.Policy.IncidentPreference}}
        result = NewRelicApiRequest(key=model.ApiKey, template=os.path.abspath(os.getcwd()) + "/newrelic_alerts_policy/queries/PolicyCreate.gql", params=params)

        model.Policy.Id = result['alertsPolicyCreate']['id']

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


    LOG.info("Beginning update handler for {}: {}".format(TYPE_NAME, model.Policy.Name)) 

    try:

        if model.Policy.Id == None:
            raise exceptions.NotFound("Policy ID", model.Policy.Id)
        else:

            progress.resourceModel = model
            progress.status = OperationStatus.SUCCESS

            params = {"accountId": model.AccountId, "id": model.Policy.Id, "alertsPolicyUpdateInput": {"name": model.Policy.Name, "incidentPreference": model.Policy.IncidentPreference}}
            result = NewRelicApiRequest(key=model.ApiKey, template=os.path.abspath(os.getcwd()) + "/newrelic_alerts_policy/queries/PolicyUpdate.gql", params=params)

            model.Policy.Name = result['alertsPolicyUpdate']['name']
            model.Policy.IncidentPreference = result['alertsPolicyUpdate']['incidentPreference']
            model.Policy.Id = result['alertsPolicyUpdate']['id']
            
            return read_handler(session, request, callback_context)

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
    
    LOG.info("Beginning create handler for {}: {}".format(TYPE_NAME, model.Policy.Name))

    try:

        params = {"accountId": model.AccountId, "id": model.Policy.Id}
        result = NewRelicApiRequest(key=model.ApiKey, template=os.path.abspath(os.getcwd()) + "/newrelic_alerts_policy/queries/PolicyDelete.gql", params=params)

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
    
    LOG.info("Beginning read handler for {}: {}".format(TYPE_NAME, model.Policy.Name))

    try: 

        params = {"accountId": model.AccountId, "id": model.Policy.Id}
        result = NewRelicApiRequest(key=model.ApiKey, template=os.path.abspath(os.getcwd()) + "/newrelic_alerts_policy/queries/PolicyRead.gql", params=params)

        policy = result["actor"]["account"]["alerts"]["policy"]

        model.Policy.Name = policy["name"]
        model.Policy.Id = policy["id"]
        model.Policy.IncidentPreference = policy["incidentPreference"]

        return ProgressEvent(
            status=OperationStatus.SUCCESS,
            resourceModel=model,
        )

    except:
        raise 



