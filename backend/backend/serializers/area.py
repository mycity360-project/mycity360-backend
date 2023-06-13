from rest_framework import serializers
from ..models.area import Area
from ..serializers.location import LocationSerializer


class AreaSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)

    @classmethod
    def serialize_data(cls, data):
        return dict(
            location=dict(
                id=data.location_id,
                name=data.location.name,
            ),
            created_date=data.created_date,
            updated_date=data.updated_date,
            extra_data=data.extra_data,
            is_active=data.is_active,
            id=data.id,
            name=data.name,
            pincode=data.pincode,
            is_deleted=data.is_deleted,
        )

    class Meta:
        model = Area
        fields = "__all__"
        depth = 1
