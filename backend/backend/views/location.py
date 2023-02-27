from rest_framework import status
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from oauth2_provider.decorators import protected_resource
from ..controllers import location as location_controller
from ..utils.views import response_handler


@api_view(["GET", "POST"])
@authentication_classes([])
@permission_classes([])
@response_handler()
def location_list(request):
    if request.method == "GET":
        response = location_controller.list_location()
        return response, status.HTTP_200_OK

    elif request.method == "POST":
        response = location_controller.create_location(request.data)
        return response, status.HTTP_201_CREATED


@api_view(["GET", "PUT", "DELETE"])
@authentication_classes([])
@permission_classes([])
@response_handler()
def location_details(request, pk):
    if request.method == "GET":
        response = location_controller.get_location(pk)
        return response, status.HTTP_200_OK

    elif request.method == "PUT":
        response = location_controller.update_location(pk, request.data)
        return response, status.HTTP_200_OK

    elif request.method == "DELETE":
        response = location_controller.delete_location(pk)
        return response, status.HTTP_204_NO_CONTENT
