from rest_framework import serializers
from ..models.service import Service
from ..serializers.image import ImageSerializer
from ..utils.serializer import serialize_image


class ServiceSerializer(serializers.ModelSerializer):
    images = ImageSerializer(read_only=True, many=True)

    @classmethod
    def serialize_data(cls, data):
        data["icon"] = serialize_image(data.get("icon"))
        if data.get("images"):
            data["images"] = [
                ImageSerializer.serialize_data(image)
                for image in data.get("images")
            ]
        return data

    class Meta:
        model = Service
        fields = "__all__"
        depth = 1
