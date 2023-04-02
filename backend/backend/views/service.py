from rest_framework import status
from rest_framework.decorators import (
    api_view,
)
from ..controllers import service as service_controller
from ..utils.views import response_handler
from ..constants import ADMIN_ROLE


@api_view(["GET", "POST"])
@response_handler(ADMIN_ROLE)
def service_list(request):
    if request.method == "GET":
        response = service_controller.list_service(
            is_active=request.query_params.get("is_active"),
            ordering=request.query_params.get("ordering"),
        )
        return response, status.HTTP_200_OK

    elif request.method == "POST":
        response = service_controller.create_service(request.data)
        return response, status.HTTP_201_CREATED


@api_view(["GET", "PUT", "DELETE"])
@response_handler(ADMIN_ROLE)
def service_details(request, pk):
    if request.method == "GET":
        response = service_controller.get_service(pk)
        return response, status.HTTP_200_OK

    elif request.method == "PUT":
        response = service_controller.update_service(pk, request.data)
        return response, status.HTTP_200_OK

    elif request.method == "DELETE":
        response = service_controller.delete_service(pk)
        return response, status.HTTP_204_NO_CONTENT


@api_view(["GET"])
@response_handler()
def service_list_user(request):
    if request.method == "GET":
        response = service_controller.list_service(
            is_active=request.query_params.get("is_active"),
            ordering=request.query_params.get("ordering"),
        )
        return response, status.HTTP_200_OK
