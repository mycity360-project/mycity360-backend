from rest_framework import status
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from oauth2_provider.decorators import protected_resource
from ..controllers import area as area_controller
from ..utils.views import response_handler


@api_view(["GET", "POST"])
@authentication_classes([])
@permission_classes([])
@response_handler()
def area_list(request):
    if request.method == "GET":
        response = area_controller.list_area()
        return response, status.HTTP_200_OK

    elif request.method == "POST":
        response = area_controller.create_area(request.data)
        return response, status.HTTP_201_CREATED


@api_view(["GET", "PUT", "DELETE"])
@authentication_classes([])
@permission_classes([])
@response_handler()
def area_details(request, pk):
    if request.method == "GET":
        response = area_controller.get_area(pk)
        return response, status.HTTP_200_OK

    elif request.method == "PUT":
        response = area_controller.update_area(pk, request.data)
        return response, status.HTTP_200_OK

    elif request.method == "DELETE":
        response = area_controller.delete_area(pk)
        return response, status.HTTP_204_NO_CONTENT
