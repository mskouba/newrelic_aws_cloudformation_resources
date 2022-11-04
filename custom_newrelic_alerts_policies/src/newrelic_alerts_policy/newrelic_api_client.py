import logging

from typing import Dict, Any

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from gql.transport.exceptions import TransportQueryError
from graphql.error.graphql_error import GraphQLError
from cloudformation_cli_python_lib import exceptions

LOG = logging.getLogger(__name__)

def new_relic_api_request(key: str, template: str, params: dict) -> Dict[str, Any]:
    """
    Function to handle GraphQL requests to New Relic NerdGraph API endpoints.
    Handles common error received from New Relic.
    Relies on gql library.
    """

    try:

        transport = RequestsHTTPTransport(
            url="https://api.newrelic.com/graphql",
            verify=True,
            retries=3,
            headers={"Content-Type": "application/json", "API-Key": key}
            )

        client = Client(transport=transport, fetch_schema_from_transport=True, serialize_variables=True)

        with open(template, encoding="utf-8") as query:
            query = gql(query.read())

        result = client.execute(query, variable_values=params)

        print(type(result))

        return result

    # Map common GQL Transport Query Errors from New Relic APIs to the proper exception in Cloudformation CLI.
    except TransportQueryError as err:

        if err.errors[0]["message"] == "Not Found":
            raise exceptions.NotFound("Policy ID", params["id"])

        elif err.errors[0]["extensions"]["errorClass"] == "BAD_USER_INPUT":
            raise exceptions.InvalidRequest("New Relic returned code BAD_USER_INPUT, please review inputs.")

        elif err.errors[0]["extensions"]["errorClass"] == "ACCESS_DENIED":
            raise exceptions.AccessDenied("Invalid credentials supplied, please review account ID and API Key.")

        elif err.errors[0]["extensions"]["errorClass"] == "SERVER_ERROR":
            raise exceptions.GeneralServiceException("New Relic returned server error. This could be due to an issue with New Relic's API.")

    except GraphQLError as err:
        raise exceptions.InvalidRequest("Invalid Value Specified. ", err)

    except Exception as err:
        raise exceptions.Unknown("Unkown Error Occurred: ") from err
