from rest_framework import serializers
from ..models.area import Area
from ..serializers.location import LocationSerializers


class AreaSerializers(serializers.ModelSerializer):
    location = LocationSerializers(read_only=True)

    class Meta:
        model = Area
        fields = "__all__"
