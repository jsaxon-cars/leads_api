from pyramid.request import Request
from pyramid.view import view_config

from leads_api.services import fraudnet_connector


@view_config(
    route_name='v1_lead_quality_status',
    openapi=True,
    renderer='json',
    type='GET'
)
def get_status(request: Request):
    params = request.openapi_validated.parameters
    service = params.path['service']
    request_id = params.path['id']

    # Example Success:
    # {
    #     "status": "success",
    #     "message": "There was a problem",
    #     "data": {"id": 1, "status": "ACCEPT"}
    # }

    # Example Error:
    # {
    #     "status": "error",
    #     "message": "Unable to complete operation",
    #     "errorCode": 12345
    # }
    response = dict(
        status="success",
        message="ok",
        data=dict(id=1, status="ACCEPT"))
    return response

@view_config(
    route_name='v1_lead_quality_request',
    openapi=True,
    renderer='json',
    type='POST'
)
def make_request(request: Request):
    """Gets the dealers coverage for a specific buyer, make within a zipcode"""
    # Get requests params
    params = request.openapi_validated.parameters
    service = params.path['service']
    # Get the configs



    # Example Error:
    # {
    #     "status": "error",
    #     "message": "Unable to complete operation",
    #     "errorCode": 12345
    # }

    # Example Success:
    # {
    #     "status": "success",
    #     "message": "There was a problem",
    #     "data": {"id": 1, "status": "ACCEPT"}
    # }

    response = dict(
        status="success",
        message="ok",
        data=dict(id=1, status="ACCEPT"))
    return response

