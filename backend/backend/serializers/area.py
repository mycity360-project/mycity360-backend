from rest_framework import serializers
from ..models.area import Area


class AreaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Area
