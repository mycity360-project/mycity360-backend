from rest_framework.response import Response
from rest_framework import status
from ..models.user import User
from ..serializers.user import UserSerializers
from oauth2_provider.decorators import protected_resource


def list_user():
    user = User.objects.all().filter(is_deleted=False)
    serializers = UserSerializers(user, many=True)
    return serializers.data


def create_user(data):
    user = User.objects.create(**data)
    user.set_password(data.get("password"))
    serializers = UserSerializers(user)
    return serializers.data


def update_user(pk, data):
    try:
        user = User.objects.filter(is_deleted=False).get(id=pk)
        serializers = UserSerializers(user, data)
        if serializers.is_valid():
            serializers.save()
            return serializers.data
    except User.DoesNotExist:
        # TODO:
        # Raise error
        return {
                   "id": ["user with this id does not exist"]
               }, status.HTTP_404_NOT_FOUND


def get_user(pk):
    try:
        user = User.objects.filter(is_deleted=False).get(id=pk)
        serializers = UserSerializers(user)
        return serializers.data
    except User.DoesNotExist:
        # TODO:
        # Raise error
        return {
                   "id": ["user with this id does not exist"]
               }, status.HTTP_404_NOT_FOUND


def delete_user(pk):
    try:
        user = User.objects.filter(is_deleted=False).get(pk=pk)
        return user.delete()
    except User.DoesNotExist:
        # TODO:
        # Raise error
        return {
                   "id": ["user with this id does not exist"]
               }, status.HTTP_404_NOT_FOUND