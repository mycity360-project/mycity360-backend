from rest_framework.exceptions import ValidationError
from ..models.saved_ad import SavedAd
from ..serializers.saved_ad import SavedAdSerializer
from ..constants import SAVED_AD_DOES_NOT_EXIST


def list_saved_ad(is_active=None):
    saved_ad = SavedAd.objects.all().filter(is_deleted=False)
    if is_active is not None:
        saved_ad = saved_ad.filter(is_active=is_active)
    serializers = SavedAdSerializer(saved_ad, many=True)
    return serializers.data


def create_saved_ad(data):
    saved_ad = SavedAd.objects.create(**data)
    serializers = SavedAdSerializer(saved_ad)
    return serializers.data


def update_saved_ad(pk, data):
    try:
        saved_ad = SavedAd.objects.filter(is_deleted=False).get(id=pk)
        serializers = SavedAdSerializer(saved_ad, data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return serializers.data
    except SavedAd.DoesNotExist:
        raise ValidationError(detail=SAVED_AD_DOES_NOT_EXIST)


def get_saved_ad(pk):
    try:
        saved_ad = SavedAd.objects.filter(is_deleted=False).get(id=pk)
        serializers = SavedAdSerializer(saved_ad)
        return serializers.data
    except SavedAd.DoesNotExist:
        raise ValidationError(detail=SAVED_AD_DOES_NOT_EXIST)


def delete_saved_ad(pk):
    try:
        saved_ad = SavedAd.objects.filter(is_deleted=False).get(pk=pk)
        return saved_ad.delete()
    except SavedAd.DoesNotExist:
        raise ValidationError(detail=SAVED_AD_DOES_NOT_EXIST)
