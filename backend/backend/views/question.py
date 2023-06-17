from rest_framework import status
from rest_framework.decorators import (
    api_view,
)
from ..controllers import question as question_controller
from ..utils.views import response_handler
from ..constants import ADMIN_ROLE


@api_view(["GET", "POST"])
@response_handler(ADMIN_ROLE)
def question_list(request):
    if request.method == "GET":
        response = question_controller.list_question(
            is_active=request.query_params.get("is_active"),
            category_id=request.query_params.get("category_id"),
            ordering=request.query_params.get("ordering"),
            page=request.query_params.get("page", 1),
            page_size=request.query_params.get("page_size", 100),
            search=request.query_params.get("search"),
        )
        return response, status.HTTP_200_OK

    elif request.method == "POST":
        response = question_controller.create_question(request.data)
        return response, status.HTTP_201_CREATED


@api_view(["GET", "PUT", "DELETE"])
@response_handler(ADMIN_ROLE)
def question_details(request, pk):
    if request.method == "GET":
        response = question_controller.get_question(pk)
        return response, status.HTTP_200_OK

    elif request.method == "PUT":
        response = question_controller.update_question(pk, request.data)
        return response, status.HTTP_200_OK

    elif request.method == "DELETE":
        response = question_controller.delete_question(pk)
        return response, status.HTTP_204_NO_CONTENT


@api_view(["GET"])
@response_handler()
def question_list_user(request):
    if request.method == "GET":
        response = question_controller.list_question(
            is_active=request.query_params.get("is_active"),
            category_id=request.query_params.get("category_id"),
            ordering=request.query_params.get("ordering"),
            page=request.query_params.get("page", 1),
            page_size=request.query_params.get("page_size", 100),
            search=request.query_params.get("search"),
        )
        return response, status.HTTP_200_OK
