import datetime
from django.db.models import Q

from rest_framework.exceptions import NotFound
from ..models.user import User
from ..serializers.user import UserSerializer
from ..constants import USER_DOES_NOT_EXIST
from ..utils.paginate import paginate_queryset


def list_user(
    is_active=None, page=1, page_size=10, ordering=None, search=None
):
    user = User.objects.all().filter(is_deleted=False)
    if is_active is not None:
        user = user.filter(is_active=is_active)
    if search:
        user = user.filter(
            Q(email__icontains=search)
            | Q(first_name__icontains=search)
            | Q(last_name__icontains=search)
            | Q(phone__icontains=search)
        )
    if not ordering:
        ordering = "-pk"
    user = user.order_by(ordering)
    data = paginate_queryset(queryset=user, page=page, page_size=page_size)
    # serializers = UserSerializer(data.get("results"), many=True)
    # data["results"] = serializers.data
    return data


def create_user(data, password=None):
    user = User.objects.create(**data)
    user.set_password(password)
    user.password_created_on = datetime.datetime.now()
    user.save()
    # serializers = UserSerializer(user)
    # return serializers.data
    return user


def update_user(id, data):
    try:
        user = User.objects.filter(is_deleted=False).get(id=id)
        data.pop("profile_image")
        serializers = UserSerializer(user, data)
        if serializers.is_valid(raise_exception=True):
            serializers.save(area_id=data.get("area").get("id"))
            # return serializers.data
            return user
        return serializers.errors
    except User.DoesNotExist:
        raise NotFound(detail=USER_DOES_NOT_EXIST)


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
        # serializers = UserSerializer(user)
        # return serializers.data
        return user
    except User.DoesNotExist:
        raise NotFound(detail=USER_DOES_NOT_EXIST)


def delete_user(id):
    try:
        user = User.objects.filter(is_deleted=False).get(id=id)
        return user.delete()
    except User.DoesNotExist:
        raise NotFound(detail=USER_DOES_NOT_EXIST)


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
        raise NotFound(detail=USER_DOES_NOT_EXIST)


def upload_profile_image(pk, image):
    try:
        user = User.objects.filter(is_deleted=False).get(id=pk)
        user.profile_image = image
        user.save()
        # serializers = UserSerializer(user)
        # return serializers.data
        return user
    except User.DoesNotExist:
        raise NotFound(detail=USER_DOES_NOT_EXIST)


def update_password(id, password):
    try:
        user = User.objects.filter(is_deleted=False).get(id=id)
        user.set_password(password)
        user.password_created_on = datetime.datetime.now()
        user.save()
        # serializers = UserSerializer(user)
        # return serializers.data
        return user
    except User.DoesNotExist:
        raise NotFound(detail=USER_DOES_NOT_EXIST)
