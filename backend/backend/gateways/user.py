import datetime
from rest_framework.exceptions import NotFound
from ..models.user import User
from ..serializers.user import UserSerializer


def list_user(is_active=None):
    user = User.objects.all().filter(is_deleted=False)
    if is_active is not None:
        user = user.filter(is_active=is_active)
    serializers = UserSerializer(user, many=True)
    return serializers.data


def create_user(data, password=None):
    user = User.objects.create(**data)
    user.set_password(password)
    user.password_created_on = datetime.datetime.now()
    user.save()
    serializers = UserSerializer(user)
    return serializers.data


def update_user(id, data):
    try:
        user = User.objects.filter(is_deleted=False).get(id=id)
        serializers = UserSerializer(user, data)
        if serializers.is_valid(raise_exception=True):
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
        serializers = UserSerializer(user)
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
