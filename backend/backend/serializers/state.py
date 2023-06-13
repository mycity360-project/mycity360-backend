from rest_framework import serializers
from ..models.state import State


class StateSerializer(serializers.ModelSerializer):
    @classmethod
    def serialize_data(cls, data):
        return dict(
            created_date=data.created_date,
            updated_date=data.updated_date,
            extra_data=data.extra_data,
            is_active=data.is_active,
            id=data.id,
            name=data.name,
            is_deleted=data.is_deleted,
        )

    class Meta:
        model = State
        fields = "__all__"
        depth = 1
