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

from .models import NotificationChannel, ResourceHandlerRequest, ResourceModel, _Config

from .newrelic_api_client import NewRelicApiRequest
from dataclasses import fields
import os

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)
TYPE_NAME = "NewRelic::Alerts::NotificationChannel"

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
    LOG.info("Beginning create handler for {}: {}".format(TYPE_NAME, model.NotificationChannel.Name))

    try:
        # Create notificationChannelObject to be passed to New Relic API. General format is {type: {configKey1: configValue1, configKey2: configValue2}}
        notificationChannelInput = {model.NotificationChannel.Type.lower(): {field.name[0].lower() + field.name[1:]: getattr(model.NotificationChannel.Config, field.name) for field in fields(model.NotificationChannel.Config) if getattr(model.NotificationChannel.Config, field.name) is not None}}
        notificationChannelInput[model.NotificationChannel.Type.lower()]["name"] = model.NotificationChannel.Name
   
        # Call New Relic API and return payload as result
        params = {"accountId": model.AccountId, "notificationChannelInput": notificationChannelInput}
        result = NewRelicApiRequest(key=model.ApiKey, template=os.path.abspath(os.getcwd()) + "/newrelic_alerts_notificationchannel/queries/NotificationChannelCreate.gql", params=params)

        # Add Id to model as primary identifier
        model.NotificationChannel.Id = int(result["alertsNotificationChannelCreate"]["notificationChannel"]["id"])

        LOG.info("Successfully created notification channel {}".format(result["alertsNotificationChannelCreate"]["notificationChannel"]["name"]))
        
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
    
    
    LOG.info("Beginning update handler for {}: {}".format(TYPE_NAME, model.NotificationChannel.Name))

    try:

        # Return not found error if channel ID is none
        if model.NotificationChannel.Id == None:

            raise exceptions.NotFound("Notification Channel ID", model.NotificationChannel.Id)

        else:

            # Create notificationChannelObject to be passed to New Relic API. General format is {type: {configKey1: configValue1, configKey2: configValue2}}
            notificationChannelInput = {model.NotificationChannel.Type.lower(): {field.name[0].lower() + field.name[1:]: getattr(model.NotificationChannel.Config, field.name) for field in fields(model.NotificationChannel.Config) if getattr(model.NotificationChannel.Config, field.name) is not None}}
            notificationChannelInput[model.NotificationChannel.Type.lower()]["name"] = model.NotificationChannel.Name
            
            # Call New Relic API and return payload as result
            params = {"accountId": model.AccountId, "id": model.NotificationChannel.Id, "notificationChannelInput": notificationChannelInput}
            result = NewRelicApiRequest(key=model.ApiKey, template=os.path.abspath(os.getcwd()) + "/newrelic_alerts_notificationchannel/queries/NotificationChannelUpdate.gql", params=params)

            # Check to see if error was returned in payload for a key not found
            if "alertsNotificationChannelUpdate" in result.keys():
                if "error" in result["alertsNotificationChannelUpdate"].keys():
                    if result["alertsNotificationChannelUpdate"]["error"] is not None:
                        if result["alertsNotificationChannelUpdate"]["error"]["errorType"] == 'NOT_FOUND_ERROR':
                            raise exceptions.NotFound("Notification Channel ID", params["id"])

            # Add Id to model as primary identifier (ID should not change)
            model.NotificationChannel.Id = int(result["alertsNotificationChannelUpdate"]["notificationChannel"]["id"])

            LOG.info("Successfully updated notification channel {}".format(result["alertsNotificationChannelUpdate"]["notificationChannel"]["name"]))

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

    LOG.info("Beginning delete handler for {}: {}".format(TYPE_NAME, model.NotificationChannel.Name))

    try:
        
        # Call New Relic API and return payload as result
        params = {"accountId": model.AccountId, "id": model.NotificationChannel.Id}
        result = NewRelicApiRequest(key=model.ApiKey, template=os.path.abspath(os.getcwd()) + "/newrelic_alerts_notificationchannel/queries/NotificationChannelDelete.gql", params=params)

        # Check to see if error was returned in payload for a key not found
        if "alertsNotificationChannelDelete" in result.keys():
            if "error" in result["alertsNotificationChannelDelete"].keys():
                if result["alertsNotificationChannelDelete"]["error"] is not None:
                    if result["alertsNotificationChannelDelete"]["error"]["errorType"] == 'NOT_FOUND_ERROR':
                        raise exceptions.NotFound("Notification Channel ID", params["id"])


        LOG.info("Successfully deleted notification channel {}".format(model.NotificationChannel.Id))

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
    
    LOG.info("Beginning read handler for {}: {}".format(TYPE_NAME, model.NotificationChannel.Name))

    try:

        # Call New Relic API and return payload as result, then get just the relevant info as notificationChannel for readability
        params = {"accountId": model.AccountId, "id": model.NotificationChannel.Id}
        result = NewRelicApiRequest(key=model.ApiKey, template=os.path.abspath(os.getcwd()) + "/newrelic_alerts_notificationchannel/queries/NotificationChannelRead.gql", params=params)
        notificationChannel = result["actor"]["account"]["alerts"]["notificationChannel"]

        # Write returned data to the model
        model.NotificationChannel.Id = int(notificationChannel["id"])
        model.NotificationChannel.Name = notificationChannel["name"]
        model.NotificationChannel.Type = notificationChannel["type"]
        model.NotificationChannel.Config = _Config._deserialize({key[0].upper() + key[1:]: value for key, value in notificationChannel["config"].items()})
        
        LOG.info("Successfully retrieved notification channel {}".format(model.NotificationChannel.Id))

        return ProgressEvent(status=OperationStatus.SUCCESS, resourceModel=model)

    except:
        raise 




