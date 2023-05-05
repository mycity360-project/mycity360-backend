from rest_framework import serializers
from ..models.service import Service
from ..serializers.image import ImageSerializer
from ..utils.serializer import serialize_image


class ServiceSerializer(serializers.ModelSerializer):
    images = ImageSerializer(read_only=True, many=True)

    @classmethod
    def serialize_data(cls, data):
        images = []
        if data.images:
            images = [
                ImageSerializer.serialize_data(image)
                for image in data.images.all()
            ]
        return dict(
            images=images,
            name=data.name,
            code=data.code,
            description=data.description,
            phone=data.phone,
            created_date=data.created_date,
            updated_date=data.updated_date,
            extra_data=data.extra_data,
            is_active=data.is_active,
            id=data.id,
            sequence=data.sequence,
            icon=data.icon,
        )

    class Meta:
        model = Service
        fields = "__all__"
        depth = 1
