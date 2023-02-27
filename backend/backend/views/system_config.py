from rest_framework import status
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from oauth2_provider.decorators import protected_resource
from ..controllers import system_config as system_config_controller
from ..utils.views import response_handler


@api_view(["GET", "POST"])
@authentication_classes([])
@permission_classes([])
@response_handler()
def system_config_list(request):
    if request.method == "GET":
        response = system_config_controller.list_system_config()
        return response, status.HTTP_200_OK

    elif request.method == "POST":
        response = system_config_controller.create_system_config(request.data)
        return response, status.HTTP_201_CREATED


@api_view(["GET", "PUT", "DELETE"])
@authentication_classes([])
@permission_classes([])
@response_handler()
def system_config_details(request, pk):
    if request.method == "GET":
        response = system_config_controller.get_system_config(pk)
        return response, status.HTTP_200_OK

    elif request.method == "PUT":
        response = system_config_controller.update_system_config(pk, request.data)
        return response, status.HTTP_200_OK

    elif request.method == "DELETE":
        response = system_config_controller.delete_system_config(pk)
        return response, status.HTTP_204_NO_CONTENT
