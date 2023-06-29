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


def list_user(
    is_active=None, page=1, page_size=10, ordering=None, search=None
):
    users = user_gateway.list_user(
        is_active=is_active,
        page=page,
        page_size=page_size,
        ordering=ordering,
        search=search,
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
    if kwargs.get("email"):
        try:
            user = user_gateway.get_user(email=kwargs.get("email"))
            raise ValidationError(detail=EMAIL_USER_EXIST)
        except NotFound:
            pass
    if kwargs.get("phone"):
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
            minutes=OTP_EXPIRE_MINUTES
        )
    # else:
    # kwargs["is_email_verified"] = True
    if phone_required:
        kwargs["phone_otp"] = services.generate_otp()
        kwargs["phone_expiry"] = datetime.datetime.now() + datetime.timedelta(
            minutes=OTP_EXPIRE_MINUTES
        )
    # else:
    # kwargs["is_phone_verified"] = True
    user = create_user(kwargs)
    if not phone_required:
        user["is_phone_verified"] = True
    # user = UserSerializer.serialize_data(user)
    if email_required:
        services.send_email(
            subject=EMAIL_SUBJECT,
            body=EMAIL_BODY.format(
                user.get("first_name"), kwargs.get("email_otp")
            ),
            to_email=user.get("email"),
        )
    else:
        user["is_email_verified"] = True
    if phone_required:
        # services.send_sms()
        services.send_email(
            subject=PHONE_SUBJECT,
            body=PHONE_BODY.format(
                user.get("first_name"), kwargs.get("phone_otp")
            ),
            to_email="heena4415@gmail.com, vibh1103@gmail.com, anuragchachan97@gmail.com",
        )
    else:
        user["is_phone_verified"] = True
    return user


def verify_otp(pk, client_id, email_otp=None, phone_otp=None):
    if not (email_otp or phone_otp):
        raise ValidationError(detail=OTP_REQUIRED)
    if not client_id:
        raise ValidationError(detail=CLIENT_ID_REQUIRED)
    user = user_gateway.get_user(id=pk)
    # user = UserSerializer.serialize_data(user)
    if email_otp:
        if (
            str(email_otp) != str(user.email_otp)
            or user.email_expiry.replace(tzinfo=None) < datetime.datetime.now()
        ):
            raise ValidationError(detail=EMAIL_OTP_EXPIRED)
        user.is_email_verified = True
        user.email_expiry = None
        user.email_otp = None

    if phone_otp:
        if str(phone_otp) != str(user.phone_otp) or (
            user.phone_expiry.replace(tzinfo=None) < datetime.datetime.now()
        ):
            raise ValidationError(detail=PHONE_OTP_EXPIRED)
        user.is_phone_verified = True
        user.phone_expiry = None
        user.phone_otp = None
    user_gateway.update_user(user.id, UserSerializer.serialize_org_data(user))
    access_token = oauth.generate_access_token(
        user_id=user.id, client_id=client_id
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
    email_required = False
    phone_required = False
    for key in keys:
        if key.get("key") == EMAIL_VERIFICATION_REQUIRED:
            if not user.get("is_email_verified"):
                if key.get("value") == "true":
                    updated_user = True
                    email_required = True
                    user["email_otp"] = services.generate_otp()
                    user[
                        "email_expiry"
                    ] = datetime.datetime.now() + datetime.timedelta(
                        minutes=OTP_EXPIRE_MINUTES
                    )
                    services.send_email(
                        subject=EMAIL_SUBJECT,
                        body=EMAIL_BODY.format(
                            user.get("first_name"), user.get("email_otp")
                        ),
                        to_email=user.get("email"),
                    )
                # else:
                #     user["is_email_verified"] = True
        if key.get("key") == PHONE_VERIFICATION_REQUIRED:
            if not user.get("is_phone_verified"):
                if key.get("value") == "true":
                    updated_user = True
                    phone_required = True
                    user["phone_otp"] = services.generate_otp()
                    user[
                        "phone_expiry"
                    ] = datetime.datetime.now() + datetime.timedelta(
                        minutes=OTP_EXPIRE_MINUTES
                    )
                    # services.send_sms()
                    services.send_email(
                        subject=EMAIL_SUBJECT,
                        body=EMAIL_BODY.format(
                            user.get("first_name"), user.get("phone_otp")
                        ),
                        to_email="heena4415@gmail.com, vibh1103@gmail.com, anuragchachan97@gmail.com",
                    )
                # else:
                #     user["is_phone_verified"] = True
    if updated_user:
        user = user_gateway.update_user(user.get("id"), user)
        user = UserSerializer.serialize_data(user)
        if not email_required:
            user["is_email_verified"] = True
        if not phone_required:
            user["is_phone_verified"] = True
        return user
    access_token = oauth.generate_access_token(
        user_id=user.get("id"), client_id=client_id
    )
    return oauth.get_token_json(access_token)


def upload_profile_image(pk, image):
    if not image:
        raise ValidationError(detail=FILE_REQUIRED)
    user = user_gateway.get_user(pk)
    if user.profile_image:
        delete_image(user.profile_image)
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


def forgot_password(key):
    if not key:
        raise ValidationError(detail=EMAIL_OR_PHONE_REQUIRED)
    email_user, phone_user = None, None
    try:
        email_user = UserSerializer.serialize_data(
            user_gateway.get_user(email=key)
        )
    except:
        pass
    if not email_user:
        try:
            phone_user = UserSerializer.serialize_data(
                user_gateway.get_user(phone=key)
            )
        except:
            pass
    if not (email_user or phone_user):
        raise ValidationError(detail=USER_DOES_NOT_EXIST)
    if email_user:
        email_user["email_otp"] = services.generate_otp()
        email_user[
            "email_expiry"
        ] = datetime.datetime.now() + datetime.timedelta(
            minutes=OTP_EXPIRE_MINUTES
        )
    if phone_user:
        phone_user["phone_otp"] = services.generate_otp()
        phone_user[
            "phone_expiry"
        ] = datetime.datetime.now() + datetime.timedelta(
            minutes=OTP_EXPIRE_MINUTES
        )
    response = {}
    if email_user:
        services.send_email(
            subject=EMAIL_SUBJECT,
            body=EMAIL_BODY.format(
                email_user.get("first_name"), email_user.get("email_otp")
            ),
            to_email=email_user.get("email"),
        )
        user_gateway.update_user(email_user.get("id"), email_user)
        response = {"email": email_user.get("email")}
    if phone_user:
        # services.send_sms()
        services.send_email(
            subject=PHONE_SUBJECT,
            body=PHONE_BODY.format(
                phone_user.get("first_name"), phone_user.get("phone_otp")
            ),
            to_email="heena4415@gmail.com, vibh1103@gmail.com, anuragchachan97@gmail.com",
        )
        user_gateway.update_user(phone_user.get("id"), phone_user)
        response = {"phone": phone_user.get("phone")}
    return response


def reset_password(otp, password, email=None, phone=None):
    if not otp:
        raise ValidationError(detail=OTP_REQUIRED)
    if not password:
        raise ValidationError(detail=PASSWORD_REQUIRED)
    if not (email or phone):
        raise ValidationError(detail=OTP_REQUIRED)
    if email:
        user = UserSerializer.serialize_org_data(
            user_gateway.get_user(email=email)
        )
        if (
            str(otp) != str(user.get("email_otp"))
            or user.get("email_expiry").replace(tzinfo=None)
            < datetime.datetime.now()
        ):
            raise ValidationError(detail=EMAIL_OTP_EXPIRED)
        user["is_email_verified"] = True
        user["email_expiry"] = None
        user["email_otp"] = None
        user_gateway.update_user(user.get("id"), user)
    else:
        user = UserSerializer.serialize_org_data(
            user_gateway.get_user(phone=phone)
        )
        if str(otp) != str(user.get("phone_otp")) or (
            user.get("phone_expiry").replace(tzinfo=None)
            < datetime.datetime.now()
        ):
            raise ValidationError(detail=PHONE_OTP_EXPIRED)
        user["is_phone_verified"] = True
        user["phone_expiry"] = None
        user["phone_otp"] = None
        user_gateway.update_user(user.get("id"), user)
    user_gateway.update_password(user.get("id"), password)
    # access_token = oauth.generate_access_token(
    #     user_id=user.get("id"), client_id=client_id
    # )
    # return oauth.get_token_json(access_token)
    return {"message": PASSWORD_CHANGED}


def resend_otp(pk):
    user = user_gateway.get_user(id=pk)
    user = UserSerializer.serialize_org_data(user)
    keys = system_config_gateway.list_system_config(
        keys=[EMAIL_VERIFICATION_REQUIRED, PHONE_VERIFICATION_REQUIRED]
    )
    keys = [SystemConfigSerializer.serialize_data(data) for data in keys]
    if user.get("is_email_verified") and user.get("is_phone_verified"):
        raise ValidationError(detail=USER_VERIFIED)
    for key in keys:
        if key.get("key") == EMAIL_VERIFICATION_REQUIRED:
            if not user.get("is_email_verified"):
                if key.get("value") == "true":
                    user["email_otp"] = services.generate_otp()
                    user[
                        "email_expiry"
                    ] = datetime.datetime.now() + datetime.timedelta(
                        minutes=OTP_EXPIRE_MINUTES
                    )
                    services.send_email(
                        subject=EMAIL_SUBJECT,
                        body=EMAIL_BODY.format(
                            user.get("first_name"), user.get("email_otp")
                        ),
                        to_email=user.get("email"),
                    )
                # else:
                #     user["is_email_verified"] = True
        if key.get("key") == PHONE_VERIFICATION_REQUIRED:
            if not user.get("is_phone_verified"):
                if key.get("value") == "true":
                    user["phone_otp"] = services.generate_otp()
                    user[
                        "phone_expiry"
                    ] = datetime.datetime.now() + datetime.timedelta(
                        minutes=OTP_EXPIRE_MINUTES
                    )
                    # services.send_sms()
                    services.send_email(
                        subject=PHONE_SUBJECT,
                        body=PHONE_BODY.format(
                            user.get("first_name"), user.get("phone_otp")
                        ),
                        to_email="heena4415@gmail.com, vibh1103@gmail.com, anuragchachan97@gmail.com",
                    )
                # else:
                #     user["is_phone_verified"] = True
    user_gateway.update_user(user.get("id"), user)
    return {"message": OTP_SENT}


def delete_account_request(key):
    if not key:
        raise ValidationError(detail=EMAIL_OR_PHONE_REQUIRED)
    user = None
    try:
        user = UserSerializer.serialize_data(
            user_gateway.get_user(email=key)
        )
    except:
        pass
    if not user:
        try:
            user = UserSerializer.serialize_data(
                user_gateway.get_user(phone=key)
            )
        except:
            pass
    if not user:
        return {"message": "Success"}
    services.send_email(
        subject=DELETE_EMAIL_SUBJECT,
        body=DELETE_EMAIL_BODY.format(
            user.get("first_name"),
            user.get("phone"),
            user.get("email"),
        ),
        to_email=SUPPORT_EMAILS,
    ),
    return {"message": "Success"}
