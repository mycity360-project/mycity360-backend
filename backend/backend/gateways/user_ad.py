from rest_framework.exceptions import ValidationError
from django.db.models import Q
from ..models.user_ad import UserAd
from ..serializers.user_ad import UserAdSerializer
from ..utils.paginate import paginate_queryset


def list_user_ad(
    is_active=None,
    is_featured=None,
    category_id=None,
    user_id=None,
    area_id=None,
    location_id=None,
    page=1,
    page_size=10,
    ordering=None,
    search=None,
):
    user_ad = UserAd.objects.all().filter(is_deleted=False)
    if is_active is not None:
        user_ad = user_ad.filter(is_active=is_active)
    if is_featured is not None:
        user_ad = user_ad.filter(is_featured=is_featured)
    if category_id:
        user_ad = user_ad.filter(category_id=category_id)
    if user_id:
        user_ad = user_ad.filter(user_id=user_id)
    if area_id:
        user_ad = user_ad.filter(area_id=area_id)
    if location_id:
        user_ad = user_ad.filter(area__location_id=location_id)
    if search:
        user_ad = user_ad.filter(
            Q(name=search)
            | Q(code=search)
            | Q(description=search)
            | Q(category__name=search)
            | Q(tags__contains=search)
        )
    if not ordering:
        ordering = "-pk"
    user_ad = user_ad.order_by(ordering)
    data = paginate_queryset(queryset=user_ad, page=page, page_size=page_size)
    serializers = UserAdSerializer(data.get("results"), many=True)
    data["results"] = serializers.data
    return data


def create_user_ad(data):
    images = data.pop("images")
    user_ad = UserAd.objects.create(**data)
    for image in images:
        user_ad.images.add(image.get("id"))
    user_ad.save()
    serializers = UserAdSerializer(user_ad)
    return serializers.data


def update_user_ad(pk, data):
    try:
        user_ad = UserAd.objects.filter(is_deleted=False).get(id=pk)
        serializers = UserAdSerializer(user_ad, data)
        user_ad.images.clear()
        for image in data.get("images"):
            user_ad.images.add(image.get("id"))
        if serializers.is_valid(raise_exception=True):
            kwargs = {}
            if data.get("category", {}):
                kwargs["category_id"] = data.get("category").get("id")
            if data.get("area", {}):
                kwargs["area_id"] = data.get("area").get("id")
            serializers.save(**kwargs)
            return serializers.data
    except UserAd.DoesNotExist:
        raise ValidationError(detail="UserAd with this id does not exist")


def get_user_ad(pk):
    try:
        user_ad = UserAd.objects.filter(is_deleted=False).get(id=pk)
        serializers = UserAdSerializer(user_ad)
        return serializers.data
    except UserAd.DoesNotExist:
        raise ValidationError(detail="UserAd with this id does not exist")


def delete_user_ad(pk):
    try:
        user_ad = UserAd.objects.filter(is_deleted=False).get(pk=pk)
        return user_ad.delete()
    except UserAd.DoesNotExist:
        raise ValidationError(detail="UserAd with this id does not exist")
