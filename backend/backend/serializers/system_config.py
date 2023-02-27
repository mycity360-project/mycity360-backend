from rest_framework import serializers
from ..models.system_config import SystemConfig


class SystemConfigSerializers(serializers.ModelSerializer):
    class Meta:
        model = SystemConfig
        fields = "__all__"
