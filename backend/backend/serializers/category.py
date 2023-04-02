from rest_framework import serializers
from ..models.category import Category
from ..utils.serializer import serialize_image


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        depth = 1


class CategorySerializer(serializers.ModelSerializer):
    category = SubCategorySerializer(read_only=True)

    @classmethod
    def serialize_data(cls, data):
        data["icon"] = serialize_image(data.get("icon"))
        if data.get("category"):
            data["category"] = CategorySerializer.serialize_data(
                data["category"]
            )
        return data

    class Meta:
        model = Category
        fields = "__all__"
        depth = 1
