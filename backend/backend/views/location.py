from rest_framework import status
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from ..controllers import location as location_controller
from ..utils.views import response_handler
from ..constants import ADMIN_ROLE


@api_view(["GET", "POST"])
@response_handler([ADMIN_ROLE])
def location_list(request):
    if request.method == "GET":
        response = location_controller.list_location(
            is_active=request.query_params.get("is_active", True),
            state_id=request.query_params.get("state_id"),
            ordering=request.query_params.get("ordering"),
            search=request.query_params.get("search"),
        )
        return response, status.HTTP_200_OK

    elif request.method == "POST":
        response = location_controller.create_location(request.data)
        return response, status.HTTP_201_CREATED


@api_view(["GET", "PUT", "DELETE"])
@response_handler([ADMIN_ROLE])
def location_details(request, pk):
    if request.method == "GET":
        response = location_controller.get_location(pk=pk)
        return response, status.HTTP_200_OK

    elif request.method == "PUT":
        response = location_controller.update_location(pk, request.data)
        return response, status.HTTP_200_OK

    elif request.method == "DELETE":
        response = location_controller.delete_location(pk)
        return response, status.HTTP_204_NO_CONTENT


@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
@response_handler(login_required=False)
def public_location_list(request):
    if request.method == "GET":
        response = location_controller.list_location(
            is_active=request.query_params.get("is_active", True),
            state_id=request.query_params.get("state_id"),
            ordering=request.query_params.get("ordering"),
            search=request.query_params.get("search"),
        )
        return response, status.HTTP_200_OK
