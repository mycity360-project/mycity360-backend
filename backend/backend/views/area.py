from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import AllowAny
from ..models.user import User
from ..serializers.user import UserSerializers
from oauth2_provider.decorators import protected_resource


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def user_list(request):

    if request.method == "GET":
        user = User.objects.all()
        serializers = UserSerializers(user, many=True)
        return Response(serializers.data)

    elif request.method == "POST":
        serializers = UserSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@protected_resource()
def user_details(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializers = UserSerializers(User)
        return Response(serializers.data)

    elif request.method == "PUT":
        serializers = UserSerializers(User, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
