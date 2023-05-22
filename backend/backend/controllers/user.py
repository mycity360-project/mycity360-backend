import datetime
from rest_framework.exceptions import ValidationError
from ..constants import FILE_REQUIRED
from rest_framework.exceptions import ValidationError, NotFound
from ..serializers.user import UserSerializer
from ..gateways import user as user_gateway
from ..gateways import system_config as system_config_gateway
from ..constants import *
from ..utils import services, oauth
from dateutil import parser
from ..serializers.system_config import SystemConfigSerializer
from ..utils.google_api import upload_to_local, delete_image


def list_user(is_active=None, page=1, page_size=10, ordering=None):
    users = user_gateway.list_user(
        is_active=is_active, page=page, page_size=page_size, ordering=ordering
    )
    users["results"] = [
        UserSerializer.serialize_data(user) for user in users.get("results")
    ]
    return users


def create_user(data):
    if "id" in data:
        data.pop("id")
    if not data.get("username"):
        data["username"] = data.get("phone")
    data["role"] = "User"
    serializers = UserSerializer(data=data)
    if serializers.is_valid(raise_exception=True):
        if data.get("area").get("id"):
            area = data.pop("area")
            data["area_id"] = area.get("id")
        password = data.pop("password")
        user = user_gateway.create_user(data, password)
        return UserSerializer.serialize_data(user)


def get_user(id):
    user = user_gateway.get_user(id)
    return UserSerializer.serialize_data(user)


def update_user(id, data):
    if "id" in data:
        data.pop("id")
    user = user_gateway.update_user(id, data)
    return UserSerializer.serialize_data(user)


def delete_user(id):
    user = user_gateway.delete_user(id)
    return user


def signup(**kwargs):
    if not (kwargs.get("email") or kwargs.get("phone")):
        raise ValidationError(detail=EMAIL_OR_PHONE_REQUIRED)
    if not kwargs.get("area") or (
        kwargs.get("area") and not kwargs.get("area").get("id")
    ):
        raise ValidationError(detail=AREA_REQUIRED)
    try:
        user = user_gateway.get_user(email=kwargs.get("email"))
        raise ValidationError(detail=EMAIL_USER_EXIST)
    except NotFound:
        pass
    try:
        user = user_gateway.get_user(phone=kwargs.get("phone"))
        raise ValidationError(detail=PHONE_USER_EXIST)
    except NotFound:
        pass
    keys = system_config_gateway.list_system_config(
        keys=[EMAIL_VERIFICATION_REQUIRED, PHONE_VERIFICATION_REQUIRED]
    )
    keys = [SystemConfigSerializer.serialize_data(data) for data in keys]
    email_required = False
    phone_required = False
    for key in keys:
        if key.get("key") == EMAIL_VERIFICATION_REQUIRED:
            if key.get("value") == "true":
                email_required = True
            continue
        if key.get("key") == PHONE_VERIFICATION_REQUIRED:
            if key.get("value") == "true":
                phone_required = True
    if email_required:
        kwargs["email_otp"] = services.generate_otp()
        kwargs["email_expiry"] = datetime.datetime.now() + datetime.timedelta(
            minutes=1
        )
    else:
        kwargs["is_email_verified"] = True
    if phone_required:
        kwargs["phone_otp"] = services.generate_otp()
        kwargs["phone_expiry"] = datetime.datetime.now() + datetime.timedelta(
            minutes=1
        )
    else:
        kwargs["is_phone_verified"] = True
    user = create_user(kwargs)
    # user = UserSerializer.serialize_data(user)
    if email_required:
        services.send_email(
            subject=EMAIL_SUBJECT,
            body=EMAIL_BODY.format(
                user.get("first_name"), user.get("email_otp")
            ),
            to_email=user.get("email"),
        )
    if phone_required:
        services.send_sms()
    return user


def verify_otp(pk, client_id, email_otp=None, phone_otp=None):
    if not (email_otp or phone_otp):
        raise ValidationError(detail=OTP_REQUIRED)
    if not client_id:
        raise ValidationError(detail=CLIENT_ID_REQUIRED)
    user = user_gateway.get_user(id=pk)
    user = UserSerializer.serialize_data(user)
    if email_otp:
        if (
            str(email_otp) != str(user.get("email_otp"))
            or parser.parse(user.get("email_expiry")).replace(tzinfo=None)
            < datetime.datetime.now()
        ):
            raise ValidationError(detail=EMAIL_OTP_EXPIRED)
        user["is_email_verified"] = True
        user["email_expiry"] = None
        user["email_otp"] = None

    if phone_otp:
        if str(phone_otp) != str(user.get("phone_otp")) or (
            parser.parse(user.get("phone_expiry")).replace(tzinfo=None)
            < datetime.datetime.now()
        ):
            raise ValidationError(detail=PHONE_OTP_EXPIRED)
        user["is_phone_verified"] = True
        user["phone_expiry"] = None
        user["phone_otp"] = None
    user_gateway.update_user(user.get("id"), user)
    access_token = oauth.generate_access_token(
        user_id=user.get("id"), client_id=client_id
    )
    return oauth.get_token_json(access_token)


def login(email, password, client_id):
    if not email:
        raise ValidationError(detail=EMAIL_OR_PHONE_REQUIRED)
    if not client_id:
        raise ValidationError(detail=CLIENT_ID_REQUIRED)
    if not password:
        raise ValidationError(detail=PASSWORD_REQUIRED)
    user = None
    try:
        user = user_gateway.get_user(email=email)
    except:
        pass
    try:
        user = user_gateway.get_user(phone=email)
    except:
        pass
    if not user:
        raise ValidationError(detail=USER_DOES_NOT_EXIST)
    user = UserSerializer.serialize_data(user)
    if not user_gateway.verify_password(password=password, id=user.get("id")):
        raise ValidationError(detail=PASSWORD_VERIFICATION_FAILED)
    keys = system_config_gateway.list_system_config(
        keys=[EMAIL_VERIFICATION_REQUIRED, PHONE_VERIFICATION_REQUIRED]
    )
    keys = [SystemConfigSerializer.serialize_data(data) for data in keys]
    updated_user = False
    for key in keys:
        if key.get("key") == EMAIL_VERIFICATION_REQUIRED:
            if not user.get("is_email_verified"):
                updated_user = True
                if key.get("value") == "true":

                    user["email_otp"] = services.generate_otp()
                    user[
                        "email_expiry"
                    ] = datetime.datetime.now() + datetime.timedelta(minutes=1)
                    services.send_email(
                        subject=EMAIL_SUBJECT,
                        body=EMAIL_BODY.format(
                            user.get("first_name"), user.get("email_otp")
                        ),
                        to_email=user.get("email"),
                    )
                else:
                    user["is_email_verified"] = True
        if key.get("key") == PHONE_VERIFICATION_REQUIRED:
            if not user.get("is_phone_verified"):
                updated_user = True
                if key.get("value") == "true":

                    user["phone_otp"] = services.generate_otp()
                    user[
                        "phone_expiry"
                    ] = datetime.datetime.now() + datetime.timedelta(minutes=1)
                    services.send_sms()
                else:
                    user["is_phone_verified"] = True
    if updated_user:
        user = user_gateway.update_user(user.get("id"), user)
    if not user.get("is_phone_verified") or not user.get("is_email_verified"):
        return UserSerializer.serialize_data(user)
    access_token = oauth.generate_access_token(
        user_id=user.get("id"), client_id=client_id
    )
    return oauth.get_token_json(access_token)


def upload_profile_image(pk, image):
    if not image:
        raise ValidationError(detail=FILE_REQUIRED)
    user = user_gateway.get_user(pk)
    if user.get("icon"):
        delete_image(user.get("profile_image"))
    user = user_gateway.upload_profile_image(
        pk, upload_to_local(image, folder="user")
    )
    return UserSerializer.serialize_data(user)


def change_password(id, current_password, new_password):
    if current_password == new_password:
        raise ValidationError(detail=NEW_PASSWORD_IS_SAME)
    if not user_gateway.verify_password(password=current_password, id=id):
        raise ValidationError(detail=PASSWORD_VERIFICATION_FAILED)
    user = user_gateway.update_password(id, new_password)
    return UserSerializer.serialize_data(user)
