from rest_framework import status
from rest_framework.decorators import (
    api_view,
)
from ..controllers import user_ad as user_ad_controller
from ..utils.views import response_handler


@api_view(["GET", "POST"])
@response_handler()
def user_ad_list(request):
    if request.method == "GET":
        response = user_ad_controller.list_user_ad(
            is_active=request.query_params.get("is_active"),
            is_featured=request.query_params.get("is_featured"),
            category_id=request.query_params.get("category_id"),
            user_id=request.query_params.get("user_id"),
            area_id=request.query_params.get("area_id"),
            location_id=request.query_params.get("location_id"),
        )
        return response, status.HTTP_200_OK

    elif request.method == "POST":
        response = user_ad_controller.create_user_ad(request.data)
        return response, status.HTTP_201_CREATED


@api_view(["GET", "PUT", "DELETE"])
@response_handler()
def user_ad_details(request, pk):
    if request.method == "GET":
        response = user_ad_controller.get_user_ad(pk)
        return response, status.HTTP_200_OK

    elif request.method == "PUT":
        response = user_ad_controller.update_user_ad(pk, request.data)
        return response, status.HTTP_200_OK

    elif request.method == "DELETE":
        response = user_ad_controller.delete_user_ad(pk)
        return response, status.HTTP_204_NO_CONTENT
