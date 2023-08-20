from rest_framework import status
from rest_framework.decorators import (
    api_view,
)
from ..controllers import banner as banner_controller
from ..utils.views import response_handler
from ..constants import ADMIN_ROLE, USER_ROLE, GUEST_ROLE


@api_view(["GET", "POST"])
@response_handler([ADMIN_ROLE])
def banner_list(request):
    if request.method == "GET":
        response = banner_controller.list_banner(
            is_active=request.query_params.get("is_active", True),
            area_id=request.query_params.get("area_id"),
            ordering=request.query_params.get("ordering"),
            page=request.query_params.get("page", 1),
            page_size=request.query_params.get("page_size", 10),
            search=request.query_params.get("search"),
        )
        return response, status.HTTP_200_OK

    elif request.method == "POST":
        response = banner_controller.create_banner(request.data)
        return response, status.HTTP_201_CREATED


@api_view(["GET", "PUT", "DELETE"])
@response_handler([ADMIN_ROLE])
def banner_details(request, pk):
    if request.method == "GET":
        response = banner_controller.get_banner(pk=pk)
        return response, status.HTTP_200_OK

    elif request.method == "PUT":
        response = banner_controller.update_banner(pk, request.data)
        return response, status.HTTP_200_OK

    elif request.method == "DELETE":
        response = banner_controller.delete_banner(pk)
        return response, status.HTTP_204_NO_CONTENT


@api_view(["GET"])
@response_handler([USER_ROLE, GUEST_ROLE])
def banner_list_user(request):
    if request.method == "GET":
        response = banner_controller.list_banner(
            is_active=request.query_params.get("is_active", True),
            area_id=request.query_params.get("area_id"),
            ordering=request.query_params.get("ordering"),
            page=request.query_params.get("page", 1),
            page_size=request.query_params.get("page_size", 10),
            search=request.query_params.get("search"),
        )
        return response, status.HTTP_200_OK


@api_view(["POST"])
@response_handler([ADMIN_ROLE])
def banner_image_upload(request, pk):
    response = banner_controller.upload_image(pk, request.FILES.get("file"))
    return response, status.HTTP_200_OK
