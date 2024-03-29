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

        return dict(
            category=dict(
                id=data.category_id,
                name=data.category.name,
            )
            if data.category
            else None,
            created_date=data.created_date,
            updated_date=data.updated_date,
            extra_data=data.extra_data,
            is_active=data.is_active,
            id=data.id,
            name=data.name,
            phone=data.phone,
            sequence=data.sequence,
            icon=data.icon,
            is_price=data.is_price,
            price_limit=data.price_limit,
            is_deleted=data.is_deleted,
        )

    class Meta:
        model = Category
        fields = "__all__"
        depth = 1
