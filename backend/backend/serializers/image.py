from rest_framework import serializers
from ..models.image import Image
from ..utils.serializer import serialize_image


class ImageSerializer(serializers.ModelSerializer):
    @classmethod
    def serialize_data(cls, data):
        return dict(
            id=data.get("id"), image=serialize_image(data.get("image"))
        )

    class Meta:
        model = Image
        fields = "__all__"
        depth = 1
