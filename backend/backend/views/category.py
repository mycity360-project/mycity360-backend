from rest_framework import status
from rest_framework.decorators import (
    api_view,
)
from ..controllers import category as category_controller
from ..utils.views import response_handler
from ..constants import ADMIN_ROLE


@api_view(["GET", "POST"])
@response_handler(ADMIN_ROLE)
def category_list(request):
    if request.method == "GET":
        response = category_controller.list_category(
            is_active=request.query_params.get("is_active")
        )
        return response, status.HTTP_200_OK

    elif request.method == "POST":
        response = category_controller.create_category(request.data)
        return response, status.HTTP_201_CREATED


@api_view(["GET", "PUT", "DELETE"])
@response_handler(ADMIN_ROLE)
def category_details(request, pk):
    if request.method == "GET":
        response = category_controller.get_category(pk)
        return response, status.HTTP_200_OK

    elif request.method == "PUT":
        response = category_controller.update_category(pk, request.data)
        return response, status.HTTP_200_OK

    elif request.method == "DELETE":
        response = category_controller.delete_category(pk)
        return response, status.HTTP_204_NO_CONTENT


@api_view(["GET"])
@response_handler()
def category_list_user(request):
    if request.method == "GET":
        response = category_controller.list_category(
            is_active=request.query_params.get("is_active")
        )
        return response, status.HTTP_200_OK