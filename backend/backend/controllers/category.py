from rest_framework.exceptions import ValidationError
from ..constants import FILE_REQUIRED
from ..serializers.category import CategorySerializer
from ..gateways import category as category_gateway
from ..utils.cache import cache
from ..utils.google_api import upload_to_local, delete_image


@cache(invalidate=False)
def list_category(
    is_active=None,
    category_id=None,
    page=1,
    page_size=10,
    ordering=None,
    parent=None,
):
    category = category_gateway.list_category(
        is_active=is_active,
        category_id=category_id,
        page=page,
        page_size=page_size,
        ordering=ordering,
        parent=parent,
    )
    category["results"] = [
        CategorySerializer.serialize_data(data)
        for data in category.get("results")
    ]
    return category


@cache(invalidate=True)
def create_category(data):
    if "id" in data:
        data.pop("id")
    serializers = CategorySerializer(data=data)
    if serializers.is_valid(raise_exception=True):
        category = category_gateway.create_category(data)
        return CategorySerializer.serialize_data(category)


@cache(invalidate=False)
def get_category(pk):
    category = category_gateway.get_category(pk)
    return CategorySerializer.serialize_data(category)


@cache(invalidate=True)
def update_category(pk, data):
    if "id" in data:
        data.pop("id")
    category = category_gateway.update_category(pk, data)
    return CategorySerializer.serialize_data(category)


@cache(invalidate=True)
def delete_category(pk):
    category = category_gateway.get_category(pk)
    if category.icon:
        delete_image(category.icon)
    category = category_gateway.delete_category(pk)
    return category


@cache(invalidate=True)
def upload_icon(pk, icon):
    if not icon:
        raise ValidationError(detail=FILE_REQUIRED)
    category = category_gateway.get_category(pk)
    if category.icon:
        delete_image(category.icon)
    category = category_gateway.upload_icon(
        pk, upload_to_local(icon, folder="category")
    )
    return CategorySerializer.serialize_data(category)
