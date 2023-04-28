from rest_framework.exceptions import ValidationError
from ..models.saved_ad import SavedAd
from ..serializers.saved_ad import SavedAdSerializer
from ..constants import SAVED_AD_DOES_NOT_EXIST
from ..utils.paginate import paginate_queryset


def list_saved_ad(
    is_active=None,
    user_id=None,
    user_ad_id=None,
    page=1,
    page_size=10,
    ordering=None,
):
    saved_ad = SavedAd.objects.all().filter(is_deleted=False)
    if is_active is not None:
        saved_ad = saved_ad.filter(is_active=is_active)
    if user_id is not None:
        saved_ad = saved_ad.filter(user_id=user_id)
    if user_ad_id is not None:
        saved_ad = saved_ad.filter(user_ad_id=user_ad_id)
    if not ordering:
        ordering = "-pk"
    saved_ad = saved_ad.order_by(ordering)
    data = paginate_queryset(queryset=saved_ad, page=page, page_size=page_size)
    # serializers = SavedAdSerializer(data.get("results"), many=True)
    # data["results"] = serializers.data
    return data


def create_saved_ad(data):
    saved_ad = SavedAd.objects.create(**data)
    # serializers = SavedAdSerializer(saved_ad)
    # return serializers.data
    return saved_ad


def update_saved_ad(pk, data):
    try:
        saved_ad = SavedAd.objects.filter(is_deleted=False).get(id=pk)
        serializers = SavedAdSerializer(saved_ad, data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            # return serializers.data
            return saved_ad
    except SavedAd.DoesNotExist:
        raise ValidationError(detail=SAVED_AD_DOES_NOT_EXIST)


def get_saved_ad(pk):
    try:
        saved_ad = SavedAd.objects.filter(is_deleted=False).get(id=pk)
        # serializers = SavedAdSerializer(saved_ad)
        # return serializers.data
        return saved_ad
    except SavedAd.DoesNotExist:
        raise ValidationError(detail=SAVED_AD_DOES_NOT_EXIST)


def delete_saved_ad(pk):
    try:
        saved_ad = SavedAd.objects.filter(is_deleted=False).get(pk=pk)
        return saved_ad.delete()
    except SavedAd.DoesNotExist:
        raise ValidationError(detail=SAVED_AD_DOES_NOT_EXIST)
