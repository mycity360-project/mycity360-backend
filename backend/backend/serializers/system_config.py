from rest_framework import serializers
from ..models.system_config import SystemConfig


class SystemConfigSerializer(serializers.ModelSerializer):
    @classmethod
    def serialize_data(cls, data):
        return dict(
            created_date=data.created_date,
            updated_date=data.updated_date,
            extra_data=data.extra_data,
            is_active=data.is_active,
            id=data.id,
            key=data.key,
            value=data.value,
        )

    class Meta:
        model = SystemConfig
        fields = "__all__"
        depth = 1
