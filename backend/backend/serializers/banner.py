from rest_framework import serializers
from ..models.banner import Banner
from ..utils.serializer import serialize_image


class BannerSerializer(serializers.ModelSerializer):
    @classmethod
    def serialize_data(cls, data):
        data["image"] = serialize_image(data.get("image"))
        data["area"] = dict(id=data.get("area").get("id"))
        return data

    class Meta:
        model = Banner
        fields = "__all__"
        depth = 1
