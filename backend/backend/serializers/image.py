from rest_framework import serializers
from ..models.image import Image
from ..utils.serializer import serialize_image


class ImageSerializer(serializers.ModelSerializer):
    @classmethod
    def serialize_data(cls, data):
        return dict(
            id=data.id,
            image=data.image,
        )

    class Meta:
        model = Image
        fields = "__all__"
        depth = 1
        read_only_fields = ("image", "id")
