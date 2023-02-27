from rest_framework import serializers
from ..models.state import State


class StateSerializers(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = "__all__"
