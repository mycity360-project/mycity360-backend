from rest_framework.exceptions import ValidationError
from ..models.category import Category
from ..serializers.category import CategorySerializer


def list_category(is_active=None):
    category = Category.objects.all().filter(is_deleted=False)
    if is_active is not None:
        category = category.filter(is_active=is_active)
    serializers = CategorySerializer(category, many=True)
    return serializers.data


def create_category(data):
    category = Category.objects.create(**data)
    serializers = CategorySerializer(category)
    return serializers.data


def update_category(pk, data):
    try:
        category = Category.objects.filter(is_deleted=False).get(id=pk)
        serializers = CategorySerializer(category, data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return serializers.data
    except Category.DoesNotExist:
        raise ValidationError(detail="Category with this id does not exist")


def get_category(pk):
    try:
        category = Category.objects.filter(is_deleted=False).get(id=pk)
        serializers = CategorySerializer(category)
        return serializers.data
    except Category.DoesNotExist:
        raise ValidationError(detail="Category with this id does not exist")


def delete_category(pk):
    try:
        category = Category.objects.filter(is_deleted=False).get(pk=pk)
        return category.delete()
    except Category.DoesNotExist:
        raise ValidationError(detail="Category with this id does not exist")
