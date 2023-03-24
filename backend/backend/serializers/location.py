from rest_framework import serializers
from ..models.location import Location
from ..serializers.state import StateSerializer


class LocationSerializer(serializers.ModelSerializer):
    state = StateSerializer(read_only=True)

    class Meta:
        model = Location
        fields = "__all__"
        depth = 1
