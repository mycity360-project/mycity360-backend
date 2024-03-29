from rest_framework import status
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from ..controllers import area as area_controller
from ..utils.views import response_handler
from ..constants import ADMIN_ROLE


@api_view(["GET", "POST"])
@response_handler([ADMIN_ROLE])
def area_list(request):
    if request.method == "GET":
        response = area_controller.list_area(
            is_active=request.query_params.get("is_active", True),
            location_id=request.query_params.get("location_id"),
            ordering=request.query_params.get("ordering"),
            search=request.query_params.get("search"),
        )
        return response, status.HTTP_200_OK

    elif request.method == "POST":
        response = area_controller.create_area(request.data)
        return response, status.HTTP_201_CREATED


@api_view(["GET", "PUT", "DELETE"])
@response_handler([ADMIN_ROLE])
def area_details(request, pk):
    if request.method == "GET":
        response = area_controller.get_area(pk=pk)
        return response, status.HTTP_200_OK

    elif request.method == "PUT":
        response = area_controller.update_area(pk, request.data)
        return response, status.HTTP_200_OK

    elif request.method == "DELETE":
        response = area_controller.delete_area(pk)
        return response, status.HTTP_204_NO_CONTENT


@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
@response_handler(login_required=False)
def public_area_list(request):
    if request.method == "GET":
        response = area_controller.list_area(
            is_active=request.query_params.get("is_active"),
            location_id=request.query_params.get("location_id"),
            ordering=request.query_params.get("ordering"),
            search=request.query_params.get("search"),
        )
        return response, status.HTTP_200_OK
