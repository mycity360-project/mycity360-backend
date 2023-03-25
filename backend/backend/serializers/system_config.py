from rest_framework import serializers
from ..models.system_config import SystemConfig


class SystemConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemConfig
        fields = "__all__"
        depth = 1
