from rest_framework.exceptions import ValidationError
from ..constants import FILE_REQUIRED
from ..serializers.category import CategorySerializer
from ..gateways import category as category_gateway


def list_category(
    is_active=None, category_id=None, page=1, page_size=10, ordering=None
):
    category = category_gateway.list_category(
        is_active=is_active,
        category_id=category_id,
        page=page,
        page_size=page_size,
        ordering=ordering,
    )
    category["results"] = [
        CategorySerializer.serialize_data(data)
        for data in category.get("results")
    ]
    return category


def create_category(data):
    if "id" in data:
        data.pop("id")
    serializers = CategorySerializer(data=data)
    if serializers.is_valid(raise_exception=True):
        category = category_gateway.create_category(data)
        return CategorySerializer.serialize_data(category)


def get_category(pk):
    category = category_gateway.get_category(pk)
    return CategorySerializer.serialize_data(category)


def update_category(pk, data):
    if "id" in data:
        data.pop("id")
    category = category_gateway.update_category(pk, data)
    return CategorySerializer.serialize_data(category)


def delete_category(pk):
    category = category_gateway.delete_category(pk)
    return category


def upload_icon(pk, icon):
    if not icon:
        raise ValidationError(detail=FILE_REQUIRED)
    category = category_gateway.upload_icon(pk, icon)
    return CategorySerializer.serialize_data(category)
