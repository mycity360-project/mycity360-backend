from rest_framework import status
from rest_framework.decorators import (
    api_view,
)
from ..controllers import state as state_controller
from ..utils.views import response_handler
from ..constants import ADMIN_ROLE


@api_view(["GET", "POST"])
@response_handler(ADMIN_ROLE)
def state_list(request):
    if request.method == "GET":
        response = state_controller.list_state(
            is_active=request.query_params.get("is_active")
        )
        return response, status.HTTP_200_OK

    elif request.method == "POST":
        response = state_controller.create_state(request.data)
        return response, status.HTTP_201_CREATED


@api_view(["GET", "PUT", "DELETE"])
@response_handler(ADMIN_ROLE)
def state_details(request, pk):
    if request.method == "GET":
        response = state_controller.get_state(pk)
        return response, status.HTTP_200_OK

    elif request.method == "PUT":
        response = state_controller.update_state(pk, request.data)
        return response, status.HTTP_200_OK

    elif request.method == "DELETE":
        response = state_controller.delete_state(pk)
        return response, status.HTTP_204_NO_CONTENT
