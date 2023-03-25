from rest_framework import serializers
from ..models.area import Area
from ..serializers.location import LocationSerializer


class AreaSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)

    class Meta:
        model = Area
        fields = "__all__"
        depth = 1
