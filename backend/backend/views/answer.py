from rest_framework import status
from rest_framework.decorators import (
    api_view,
)
from ..controllers import answer as answer_controller
from ..utils.views import response_handler
from ..constants import USER_ROLE


@api_view(["GET", "POST"])
@response_handler([USER_ROLE])
def answer_list(request):
    if request.method == "GET":
        response = answer_controller.list_answer(
            is_active=request.query_params.get("is_active", True),
            question_id=request.query_params.get("question_id"),
            user_id=request.query_params.get("user_id"),
            user_ad_id=request.query_params.get("user_ad_id"),
            ordering=request.query_params.get("ordering"),
            page=request.query_params.get("page", 1),
            page_size=request.query_params.get("page_size", 10),
        )
        return response, status.HTTP_200_OK

    elif request.method == "POST":
        response = answer_controller.create_answer(request.data)
        return response, status.HTTP_201_CREATED


@api_view(["GET", "PUT", "DELETE"])
@response_handler([USER_ROLE])
def answer_details(request, pk):
    if request.method == "GET":
        response = answer_controller.get_answer(pk)
        return response, status.HTTP_200_OK

    elif request.method == "PUT":
        response = answer_controller.update_answer(pk, request.data)
        return response, status.HTTP_200_OK

    elif request.method == "DELETE":
        response = answer_controller.delete_answer(pk)
        return response, status.HTTP_204_NO_CONTENT
