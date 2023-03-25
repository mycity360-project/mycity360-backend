from rest_framework import status
from rest_framework.decorators import (
    api_view,
)
from ..controllers import saved_ad as saved_ad_controller
from ..utils.views import response_handler


@api_view(["GET", "POST"])
@response_handler()
def saved_ad_list(request):
    if request.method == "GET":
        response = saved_ad_controller.list_saved_ad(
            is_active=request.query_params.get("is_active")
        )
        return response, status.HTTP_200_OK

    elif request.method == "POST":
        response = saved_ad_controller.create_saved_ad(request.data)
        return response, status.HTTP_201_CREATED


@api_view(["GET", "PUT", "DELETE"])
@response_handler()
def saved_ad_details(request, pk):
    if request.method == "GET":
        response = saved_ad_controller.get_saved_ad(pk)
        return response, status.HTTP_200_OK

    elif request.method == "PUT":
        response = saved_ad_controller.update_saved_ad(pk, request.data)
        return response, status.HTTP_200_OK

    elif request.method == "DELETE":
        response = saved_ad_controller.delete_saved_ad(pk)
        return response, status.HTTP_204_NO_CONTENT
