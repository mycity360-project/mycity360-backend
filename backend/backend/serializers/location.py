from rest_framework import serializers
from ..models.location import Location
from ..serializers.state import State, StateSerializers


class LocationSerializers(serializers.ModelSerializer):
    state = StateSerializers(read_only=True)

    class Meta:
        model = Location
        fields = "__all__"

