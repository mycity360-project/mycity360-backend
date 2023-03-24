import datetime

from rest_framework.exceptions import ValidationError, NotFound
from ..serializers.user import UserSerializer
from ..gateways import user as user_gateway
from ..gateways import system_config as system_config_gateway
from ..constants import (
    EMAIL_VERIFICATION_REQUIRED,
    PHONE_VERIFICATION_REQUIRED,
)
from ..utils import services, oauth
from dateutil import parser


def list_user(is_active):
    users = user_gateway.list_user(is_active)
    users = [UserSerializer.serialize_data(user) for user in users]
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


def signup(client_id=None, **kwargs):
    if not client_id:
        raise ValidationError(detail="Client id is required")
    if not (kwargs.get("email") or kwargs.get("phone")):
        raise ValidationError(detail="Email or Phone is required")
    try:
        user = user_gateway.get_user(email=kwargs.get("email"))
        raise ValidationError(detail="User already exist with email")
    except NotFound:
        pass
    try:
        user = user_gateway.get_user(phone=kwargs.get("phone"))
        raise ValidationError(detail="User already exist with phone")
    except NotFound:
        pass
    keys = system_config_gateway.list_system_config(
        keys=[EMAIL_VERIFICATION_REQUIRED, PHONE_VERIFICATION_REQUIRED]
    )
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
    if phone_required:
        kwargs["phone_otp"] = services.generate_otp()
        kwargs["phone_expiry"] = datetime.datetime.now() + datetime.timedelta(
            minutes=1
        )
    user = create_user(kwargs)
    if email_required:
        services.send_email(
            subject="MyCity360 Email Verification",
            body=f"Hi {user.get('first_name')} \n This is your OTP for email verification. \n {user.get('email_otp')} \n Regards\nMyCity360 Team",
            to_email=user.get("email"),
        )
    if phone_required:
        services.send_sms()
    return UserSerializer.serialize_data(user)


def verify_otp(pk, client_id, email_otp=None, phone_otp=None):
    if not (email_otp or phone_otp):
        raise ValidationError(detail="Email OTP or Phone OTP required")
    if not client_id:
        raise ValidationError(detail="Client id is required")
    user = user_gateway.get_user(id=pk)
    if email_otp:
        if (
            email_otp != user.get("email_otp")
            or parser.parse(user.get("email_expiry")).replace(tzinfo=None)
            > datetime.datetime.now()
        ):
            raise ValidationError(detail="Email OTP Expired")
        user["is_email_verified"] = True
        user["email_expiry"] = None
        user["email_otp"] = None

    if phone_otp:
        if (
            phone_otp != user.get("phone_otp")
            or parser.parse(user.get("phone_expiry")).replace(tzinfo=None)
            > datetime.datetime.now()
        ):
            raise ValidationError(detail="Phone OTP Expired")
        user["is_phone_verified"] = True
        user["phone_expiry"] = None
        user["phone_otp"] = None
    user_gateway.update_user(user.get("id"), user)
    access_token = oauth.generate_access_token(
        user_id=user.get("id"), client_id=client_id
    )
    return oauth.get_token_json(access_token)


def login(email, phone, password, client_id):
    if not (email or phone):
        raise ValidationError(detail="Email or Phone required")
    if not client_id:
        raise ValidationError(detail="Client id is required")
    if not password:
        raise ValidationError(detail="Password is required")
    user = user_gateway.get_user(email=email, phone=phone)
    keys = system_config_gateway.list_system_config(
        keys=[EMAIL_VERIFICATION_REQUIRED, PHONE_VERIFICATION_REQUIRED]
    )
    for key in keys:
        if key.get("key") == EMAIL_VERIFICATION_REQUIRED:
            if key.get("value") == "true" and not user.get(
                "is_email_verified"
            ):
                services.send_email(
                    subject="MyCity360 Email Verification",
                    body=f"Hi {user.get('first_name')} \n This is your OTP for email verification. \n {user.get('email_otp')} \n Regards\nMyCity360 Team",
                    to_email=user.get("email"),
                )
                return user
            continue
        if key.get("key") == PHONE_VERIFICATION_REQUIRED:
            if key.get("value") == "true" and not user.get(
                "is_phone_verified"
            ):
                services.send_sms()
                return user
    if not user_gateway.verify_password(password=password, id=user.get("id")):
        raise ValidationError(detail="Password verification failed")
    access_token = oauth.generate_access_token(
        user_id=user.get("id"), client_id=client_id
    )
    return oauth.get_token_json(access_token)
