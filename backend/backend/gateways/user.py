import datetime
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import status
from ..models.user import User
from ..serializers.user import UserSerializers
from oauth2_provider.decorators import protected_resource


def list_user():
    user = User.objects.all().filter(is_deleted=False)
    serializers = UserSerializers(user, many=True)
    return serializers.data


def create_user(data, password=None):
    user = User.objects.create(**data)
    user.set_password(password)
    user.password_created_on = datetime.datetime.now()
    user.save()
    serializers = UserSerializers(user)
    return serializers.data


def update_user(id, data):
    try:
        user = User.objects.filter(is_deleted=False).get(id=id)
        serializers = UserSerializers(user, data)
        if serializers.is_valid():
            serializers.save(area_id=data.get("area").get("id"))
            return serializers.data
        return serializers.errors
    except User.DoesNotExist:
        raise NotFound(detail="User does not exist")


def get_user(id=None, email=None, phone=None):
    try:
        kwargs = dict()
        if id:
            kwargs["id"] = id
        if email:
            kwargs["email"] = email
        if phone:
            kwargs["phone"] = phone
        user = User.objects.filter(is_deleted=False).get(**kwargs)
        serializers = UserSerializers(user)
        return serializers.data
    except User.DoesNotExist:
        raise NotFound(detail="User does not exist")


def delete_user(id):
    try:
        user = User.objects.filter(is_deleted=False).get(id=id)
        return user.delete()
    except User.DoesNotExist:
        raise NotFound(detail="User does not exist")


def verify_password(password, id=None, email=None, phone=None):
    try:
        kwargs = dict()
        if id:
            kwargs["id"] = id
        if email:
            kwargs["email"] = email
        if phone:
            kwargs["phone"] = phone
        user = User.objects.filter(is_deleted=False).get(**kwargs)
        return user.check_password(password)
    except User.DoesNotExist:
        raise NotFound(detail="User does not exist")
