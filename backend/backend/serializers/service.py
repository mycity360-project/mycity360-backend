from rest_framework import serializers
from ..models.service import Service
from ..serializers.image import ImageSerializer


class ServiceSerializer(serializers.ModelSerializer):
    images = ImageSerializer(read_only=True, many=True)

    class Meta:
        model = Service
        fields = "__all__"
        depth = 1
