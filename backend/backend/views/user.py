# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import api_view
# from ..models.user import User
# from ..serializers.user import UserSerializers
# from oauth2_provider.decorators import protected_resource
# 
# 
# @api_view(["GET", "POST"])
# @protected_resource()
# def user_list(request):
#     if request.method == "GET":
#         user = User.objects.all()
#         serializers = UserSerializers(user, many=True)
#         return Response(serializers.data)
# 
#     elif request.method == "POST":
#         serializers = UserSerializers(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
# 
# 
# @api_view(["GET", "PUT", "DELETE"])
# @protected_resource()
# def user_details(request, pk):
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
# 
#     if request.method == "GET":
#         serializers = UserSerializers(User)
#         return Response(serializers.data)
# 
#     elif request.method == "PUT":
#         serializers = UserSerializers(User, request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
# 
#     elif request.method == "DELETE":
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


from rest_framework import status
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from oauth2_provider.decorators import protected_resource
from ..controllers import user as user_controller
from ..utils.views import response_handler


@api_view(["GET", "POST"])
@authentication_classes([])
@permission_classes([])
@response_handler()
def user_list(request):
    if request.method == "GET":
        response = user_controller.list_user()
        return response, status.HTTP_200_OK

    elif request.method == "POST":
        response = user_controller.create_user(request.data)
        return response, status.HTTP_201_CREATED


@api_view(["GET", "PUT", "DELETE"])
@authentication_classes([])
@permission_classes([])
@response_handler()
def user_details(request, pk):
    if request.method == "GET":
        response = user_controller.get_user(pk)
        return response, status.HTTP_200_OK

    elif request.method == "PUT":
        response = user_controller.update_user(pk, request.data)
        return response, status.HTTP_200_OK

    elif request.method == "DELETE":
        response = user_controller.delete_user(pk)
        return response, status.HTTP_204_NO_CONTENT
