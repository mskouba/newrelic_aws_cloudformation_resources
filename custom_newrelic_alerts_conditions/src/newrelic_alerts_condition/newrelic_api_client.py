import logging

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from gql.transport.exceptions import TransportQueryError
from graphql.error.graphql_error import GraphQLError
from cloudformation_cli_python_lib import exceptions

LOG = logging.getLogger(__name__)

def NewRelicApiRequest(key: str, template: str, params: dict):

    try:

        transport = RequestsHTTPTransport(
            url='https://api.newrelic.com/graphql',
            verify=True,
            retries=3,
            headers={'Content-Type': 'application/json', 'API-Key': key}
            )

        client = Client(transport=transport, fetch_schema_from_transport=True, serialize_variables=True)

        try:
            with open(template) as query:
                query = gql(query.read())
                
        except FileNotFoundError:
            raise exceptions.InternalFailure("An internal error occurred when attempting to access graphql template {}".format(template))

        result = client.execute(query, variable_values=params)

        return result

    # Map common GQL Transport Query Errors from New Relic APIs to the proper exception in Cloudformation CLI.
    except TransportQueryError as err:

        if err.errors[0]['message'] == "Not Found":
            raise exceptions.NotFound("Condition ID", params["id"])

        elif err.errors[0]["extensions"]["errorClass"] == "BAD_USER_INPUT":
            raise exceptions.InvalidRequest("New Relic Returned Code BAD_USER_INPUT")

        elif err.errors[0]["extensions"]["errorClass"] == "ACCESS_DENIED":
            raise exceptions.AccessDenied("Invalid credentials supplied, please review account ID and API Key.")

    except GraphQLError as err:
        raise exceptions.InvalidRequest("Invalid Value Specified. ", err)

    except:
        raise 
        