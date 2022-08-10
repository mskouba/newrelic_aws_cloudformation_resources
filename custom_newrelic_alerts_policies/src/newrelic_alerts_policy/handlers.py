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

    LOG.info("Beginning create handler for {}: {}".format(TYPE_NAME, model.Policy.Name))

    try:

        # Call New Relic API and return payload as result
        params = {"accountId": model.AccountId, "alertsPolicyInput": {"name": model.Policy.Name, "incidentPreference": model.Policy.IncidentPreference}}
        result = NewRelicApiRequest(key=model.ApiKey, template=os.path.abspath(os.getcwd()) + "/newrelic_alerts_policy/queries/PolicyCreate.gql", params=params)

        # Write the ID returned to the model
        model.Policy.Id = int(result['alertsPolicyCreate']['id'])

        # Call the New Relic API to add any notfication channels to the policy
        notificationChannelParams = {"accountId": model.AccountId, "id": model.Policy.Id, "notificationChannelIds": model.Policy.NotificationChannels}
        notificationChannelResult = NewRelicApiRequest(key=model.ApiKey, template=os.path.abspath(os.getcwd()) + "/newrelic_alerts_policy/queries/NotificationChannelsAddToPolicy.gql", params=notificationChannelParams)

        # Check for any errors in the payload, this is not handled by the newrelic api client function due to notification channels using a different error handling schema.
        if notificationChannelResult["alertsNotificationChannelsAddToPolicy"]["errors"] == []:

            successfulNotificationChannels = [int(x["id"]) for x in notificationChannelResult["alertsNotificationChannelsAddToPolicy"]["notificationChannels"]]
            model.Policy.NotificationChannels = successfulNotificationChannels
            LOG.info ("Notification channels added successfully")
            LOG.info("Completed create handler for {}: {}".format(TYPE_NAME, model.Policy.Name))

            return ProgressEvent(status=OperationStatus.SUCCESS, resourceModel=model)
        else:
            raise exceptions.InternalFailure("An error occurred when adding notification channel. {}".format(str(notificationChannelResult["alertsNotificationChannelsAddToPolicy"]["errors"])))
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

        # Return not found error if policy ID is none
        if model.Policy.Id == None:
            raise exceptions.NotFound("Policy ID", model.Policy.Id)
        else:

            # Call New Relic API and return payload as result
            params = {"accountId": model.AccountId, "id": model.Policy.Id, "alertsPolicyUpdateInput": {"name": model.Policy.Name, "incidentPreference": model.Policy.IncidentPreference}}
            result = NewRelicApiRequest(key=model.ApiKey, template=os.path.abspath(os.getcwd()) + "/newrelic_alerts_policy/queries/PolicyUpdate.gql", params=params)

            # Write payload data to model
            model.Policy.Name = result['alertsPolicyUpdate']['name']
            model.Policy.IncidentPreference = result['alertsPolicyUpdate']['incidentPreference']
            model.Policy.Id = int(result['alertsPolicyUpdate']['id'])

            # Compare notification channels in payload to model and determine whether any need to be added or removed
            notificationChannelsToAdd = list(set(model.Policy.NotificationChannels) - set(request.previousResourceState.Policy.NotificationChannels))
            notificationChannelsToDelete = list(set(request.previousResourceState.Policy.NotificationChannels) - set(model.Policy.NotificationChannels))
            
            # Add any notification channels that are not added yet
            if notificationChannelsToAdd != []:
                notificationChannelAddParams = {"accountId": model.AccountId, "id": model.Policy.Id, "notificationChannelIds": notificationChannelsToAdd}
                result = NewRelicApiRequest(key=model.ApiKey, template=os.path.abspath(os.getcwd()) + "/newrelic_alerts_policy/queries/NotificationChannelsAddToPolicy.gql", params=notificationChannelAddParams)

            # Remove any notification channels that are not removed yet
            if notificationChannelsToDelete != []:
                notificationChannelDeleteParams = {"accountId": model.AccountId, "id": model.Policy.Id, "notificationChannelIds": notificationChannelsToDelete}
                result = NewRelicApiRequest(key=model.ApiKey, template=os.path.abspath(os.getcwd()) + "/newrelic_alerts_policy/queries/NotificationChannelsDeleteFromPolicy.gql", params=notificationChannelDeleteParams)

            ProgressEvent(status=OperationStatus.IN_PROGRESS, resourceModel=model, callbackContext=callback_context)

            LOG.info("Update complete, initiating read handler to confirm changes took place.")
            
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
    
    LOG.info("Beginning delete handler for {}: {}".format(TYPE_NAME, model.Policy.Name))

    try:
        
        # Call New Relic API and return payload as result
        params = {"accountId": model.AccountId, "id": model.Policy.Id}
        result = NewRelicApiRequest(key=model.ApiKey, template=os.path.abspath(os.getcwd()) + "/newrelic_alerts_policy/queries/PolicyDelete.gql", params=params)

        LOG.info("Completed delete handler for {}: {}".format(TYPE_NAME, model.Policy.Name))

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
        
        # Call New Relic API and return payload as result, then get the relevant data as policy variable for readability
        params = {"accountId": model.AccountId, "id": model.Policy.Id}
        result = NewRelicApiRequest(key=model.ApiKey, template=os.path.abspath(os.getcwd()) + "/newrelic_alerts_policy/queries/PolicyRead.gql", params=params)
        policy = result["actor"]["account"]["alerts"]["policy"]

        # Write datat returned to model
        model.Policy.Name = policy["name"]
        model.Policy.Id = int(policy["id"])
        model.Policy.IncidentPreference = policy["incidentPreference"]

        # Process of reading notification channels is inefficient due to New Relic not having an API call that can recieve a policy and return the attached notification channels.
        # To accomplish this, we must pull all notification channels in the account and check whether they are attached to the policy.
        # Due to this, it can take much longer to accomplish this step than any other handler operation in this suite of resources.
        if "NotificationChannels" not in callback_context:

            # Initialize variables in context callback to reference in loop
            getNotificationChannelsParams = {"accountId": model.AccountId}
            callback_context["NotificationChannels"] = []
            callback_context["NotificationChannelsNotComplete"] = True
            callback_context["cursor"] = None

            while callback_context["NotificationChannelsNotComplete"]:

                LOG.info("Pulling notification channels to check for channels attached to policy {}".format(model.Policy.Name))
                
                # Checks for cursor to ensure pagination is handled properly and all channels are pulled
                if callback_context["cursor"] is not None:
                    getNotificationChannelsParams["cursor"] = callback_context["cursor"]

                result = NewRelicApiRequest(key=model.ApiKey, template=os.path.abspath(os.getcwd()) + "/newrelic_alerts_policy/queries/GetNotificationChannels.gql", params=getNotificationChannelsParams)

                # Checks for nextCursor field in payload, in order to determine whether loop should continue
                if result["actor"]["account"]["alerts"]["notificationChannels"]["nextCursor"] == None:
                    callback_context["NotificationChannelsNotComplete"] = False
                
                else:
                    callback_context["cursor"] = result["actor"]["account"]["alerts"]["notificationChannels"]["nextCursor"]
                    
                # Add notification channels that are attached to policy to list of notification channels
                callback_context["NotificationChannels"].extend([int(x["id"]) for x in result["actor"]["account"]["alerts"]["notificationChannels"]["channels"] if model.Policy.Id in [int(y["id"]) for y in x["associatedPolicies"]["policies"]]])
                
                ProgressEvent(status=OperationStatus.IN_PROGRESS, resourceModel=model, callbackContext=callback_context)

            # Write all found notification channels to model
            model.Policy.NotificationChannels = callback_context["NotificationChannels"]

            LOG.info("Notification channels identified and returned to model.")
        
        else:

            model.Policy.NotificationChannels = callback_context["NotificationChannels"]
            
        return ProgressEvent(
            status=OperationStatus.SUCCESS,
            resourceModel=model,
        )

    except:
        raise 



