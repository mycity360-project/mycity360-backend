from rest_framework.exceptions import ValidationError
from ..models.category import Category
from ..serializers.category import CategorySerializer
from ..constants import CATEGORY_DOES_NOT_EXIST
from ..utils.paginate import paginate_queryset


def list_category(
    is_active=None,
    category_id=None,
    page=1,
    page_size=10,
    ordering=None,
    parent=True,
    search=None,
):
    category = Category.objects.all().filter(is_deleted=False)
    if is_active is not None:
        category = category.filter(is_active=is_active)
    if category_id is not None:
        category = category.filter(category_id=category_id)
    if not category_id:
        if parent is True:
            category = category.filter(category_id__isnull=True)
        if parent is False:
            category = category.filter(category_id__isnull=False)
    if search:
        category = category.filter(name__icontains=search)
    if not ordering:
        ordering = "sequence"
    category = category.order_by(ordering)
    data = paginate_queryset(queryset=category, page=page, page_size=page_size)
    # serializers = CategorySerializer(data.get("results"), many=True)
    # data["results"] = serializers.data
    return data


def create_category(data):
    category = Category.objects.create(**data)
    # serializers = CategorySerializer(category)
    # return serializers.data
    return category


def update_category(pk, data):
    try:
        category = Category.objects.filter(is_deleted=False).get(id=pk)
        data.pop("icon")
        serializers = CategorySerializer(category, data)
        if serializers.is_valid(raise_exception=True):
            kwargs = {}
            if data.get("category", {}):
                kwargs["category_id"] = data.get("category").get("id")
            serializers.save(**kwargs)
            # return serializers.data
            return category
    except Category.DoesNotExist:
        raise ValidationError(detail=CATEGORY_DOES_NOT_EXIST)


def get_category(pk):
    try:
        category = Category.objects.filter(is_deleted=False).get(id=pk)
        # serializers = CategorySerializer(category)
        # return serializers.data
        return category
    except Category.DoesNotExist:
        raise ValidationError(detail=CATEGORY_DOES_NOT_EXIST)


def delete_category(pk):
    try:
        category = Category.objects.filter(is_deleted=False).get(pk=pk)
        return category.delete()
    except Category.DoesNotExist:
        raise ValidationError(detail=CATEGORY_DOES_NOT_EXIST)


def upload_icon(pk, icon):
    try:
        category = Category.objects.filter(is_deleted=False).get(id=pk)
        category.icon = icon
        category.save()
        # serializers = CategorySerializer(category)
        # return serializers.data
        return category
    except Category.DoesNotExist:
        raise ValidationError(detail=CATEGORY_DOES_NOT_EXIST)
