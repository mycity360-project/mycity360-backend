from rest_framework import serializers
from ..models.category import Category


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        depth = 1


class CategorySerializer(serializers.ModelSerializer):
    category = SubCategorySerializer(read_only=True)

    class Meta:
        model = Category
        fields = "__all__"
        depth = 1
