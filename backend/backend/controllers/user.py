from rest_framework.response import Response
from rest_framework import status
from ..serializers.user import UserSerializers
from oauth2_provider.decorators import protected_resource
from ..gateways import user as user_gateway


def list_user():
    user = user_gateway.list_user()
    return user


def create_user(data):
    if "id" in data:
        data.pop("id")
    serializers = UserSerializers(data=data)
    if serializers.is_valid():
        user = user_gateway.create_user(data)
        return user
    # TODO:
    # Raise error in this case
    return serializers.errors


def get_user(pk):
    user = user_gateway.get_user(pk)
    print(user)
    return user


def update_user(pk, data):
    if "id" in data:
        data.pop("id")
    user = user_gateway.update_user(pk, data)
    return user


def delete_user(pk):
    user = user_gateway.delete_user(pk)
    return user

