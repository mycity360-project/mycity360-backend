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
            created_date=data.created_date,
            updated_date=data.updated_date,
            extra_data=data.extra_data,
            is_active=data.is_active,
            id=data.id,
            email=data.email,
            phone=data.phone,
            username=data.username,
            last_login=data.last_login,
            first_name=data.first_name,
            last_name=data.last_name,
            country_code=data.country_code,
            profile_image=serialize_image(data.profile_image.url) if data.profile_image else None,
            date_joined=data.date_joined,
            is_phone_verified=data.is_phone_verified,
            is_email_verified=data.is_email_verified,
            is_gmail_login=data.is_gmail_login,
            password_updated_on=data.password_updated_on,
            failed_login_attempts=data.failed_login_attempts,
            failed_login_time=data.failed_login_time,
            current_address=data.current_address,
            role=data.role,
            area=dict(
                id=data.area_id,
                name=data.area.name,
                location=dict(
                    id=data.area.location_id,
                    name=data.area.location.name,
                ),
            ),
        )

    class Meta:
        model = User
        fields = "__all__"
        depth = 1
