from rest_framework import serializers
from ..models.user import User
from ..serializers.area import AreaSerializer
from ..utils.serializer import serialize_image


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    phone = serializers.IntegerField(required=True)
    area = AreaSerializer(read_only=True, allow_null=True)
    username = serializers.CharField()

    @classmethod
    def serialize_data(cls, data):
        return dict(
            created_date=data.get("created_date"),
            updated_date=data.get("updated_date"),
            extra_data=data.get("extra_data"),
            is_active=data.get("is_active"),
            id=data.get("id"),
            email=data.get("email"),
            phone=data.get("phone"),
            username=data.get("username"),
            last_login=data.get("last_login"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            country_code=data.get("country_code"),
            profile_image=serialize_image(data.get("profile_image")),
            date_joined=data.get("date_joined"),
            is_phone_verified=data.get("is_phone_verified"),
            is_email_verified=data.get("is_email_verified"),
            is_gmail_login=data.get("is_gmail_login"),
            password_updated_on=data.get("password_updated_on"),
            failed_login_attempts=data.get("failed_login_attempts"),
            failed_login_time=data.get("failed_login_time"),
            current_address=data.get("current_address"),
            role=data.get("role"),
            area=dict(
                id=data.get("area").get("id"),
                name=data.get("area").get("name"),
                location=dict(
                    id=data.get("area").get("location").get("id"),
                    name=data.get("area").get("location").get("name"),
                ),
            ),
        )

    class Meta:
        model = User
        fields = "__all__"
        depth = 1
