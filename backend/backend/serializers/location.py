from rest_framework import serializers
from ..models.location import Location
from ..serializers.state import StateSerializer


class LocationSerializer(serializers.ModelSerializer):
    state = StateSerializer(read_only=True)

    @classmethod
    def serialize_data(cls, data):
        return dict(
            state=dict(
                id=data.state_id,
                name=data.state.name,
            ),
            created_date=data.created_date,
            updated_date=data.updated_date,
            extra_data=data.extra_data,
            is_active=data.is_active,
            id=data.id,
            name=data.name,
        )

    class Meta:
        model = Location
        fields = "__all__"
        depth = 1
