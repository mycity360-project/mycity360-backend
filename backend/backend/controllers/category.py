from ..serializers.category import CategorySerializer
from ..gateways import category as category_gateway


def list_category(is_active=None, category_id=None):
    category = category_gateway.list_category(is_active=is_active, category_id=category_id)
    return category


def create_category(data):
    if "id" in data:
        data.pop("id")
    serializers = CategorySerializer(data=data)
    if serializers.is_valid(raise_exception=True):
        category = category_gateway.create_category(data)
        return category


def get_category(pk):
    category = category_gateway.get_category(pk)
    return category


def update_category(pk, data):
    if "id" in data:
        data.pop("id")
    category = category_gateway.update_category(pk, data)
    return category


def delete_category(pk):
    category = category_gateway.delete_category(pk)
    return category
