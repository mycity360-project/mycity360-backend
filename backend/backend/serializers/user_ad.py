import json
from rest_framework import serializers
from ..models.user_ad import UserAd
from ..serializers.image import ImageSerializer
from ..serializers.user import UserSerializer
from ..serializers.category import CategorySerializer
from ..serializers.area import AreaSerializer


class UserAdSerializer(serializers.ModelSerializer):
    images = ImageSerializer(read_only=True, many=True)
    user = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    area = AreaSerializer(read_only=True)
    tags = serializers.ListField()

    @classmethod
    def serialize_data(cls, data):
        # if data.get("images"):
        #     data["images"] = [
        #         ImageSerializer.serialize_data(image)
        #         for image in data.get("images")
        #     ]
        # return dict(
        #     images=data.get("images"),
        #     user=dict(id=data.get("user").get("id")),
        #     category=dict(id=data.get("category").get("id")),
        #     area=dict(id=data.get("area").get("id"), location=dict(id=data.get("area").get("location").get("id"))),
        #     name=data.get("name"),
        #     code=data.get("code"),
        #     tags=data.get("tags"),
        #     is_featured=data.get("is_featured"),
        #     description=data.get("description"),
        #     price=data.get("price"),
        #     created_date=data.get("created_date"),
        #     updated_date=data.get("updated_date"),
        #     extra_data=data.get("extra_data"),
        #     is_active=data.get("is_active"),
        #     id=data.get("id"),
        # )
        images = []
        if data.images:
            images = [
                ImageSerializer.serialize_data(image)
                for image in data.images.all()
            ]
        return dict(
            images=images,
            user=dict(id=data.user.id),
            category=dict(id=data.category.id),
            area=dict(
                id=data.area.id,
                name=data.area.name,
                location=dict(
                    id=data.area.location.id,
                    name=data.area.location.name,
                ),
            ),
            name=data.name,
            code=data.code,
            tags=data.tags,
            is_featured=data.is_featured,
            description=data.description,
            price=data.price,
            created_date=data.created_date,
            updated_date=data.updated_date,
            extra_data=data.extra_data,
            is_active=data.is_active,
            id=data.id,
        )

    class Meta:
        model = UserAd
        fields = "__all__"
        depth = 1
