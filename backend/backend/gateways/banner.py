from rest_framework.exceptions import ValidationError
from ..models.banner import Banner
from ..serializers.banner import BannerSerializer
from ..constants import BANNER_DOES_NOT_EXIST
from ..utils.paginate import paginate_queryset


def list_banner(
    is_active=None,
    area_id=None,
    page=1,
    page_size=10,
    ordering=None,
    search=None,
):
    banner = Banner.objects.all().filter(is_deleted=False)
    if is_active is not None:
        banner = banner.filter(is_active=is_active)
    if area_id is not None:
        banner = banner.filter(area_id=area_id)
    if search:
        banner = banner.filter(area__name__icontains=search)
    if not ordering:
        ordering = "sequence"
    banner = banner.order_by(ordering)
    data = paginate_queryset(queryset=banner, page=page, page_size=page_size)
    # serializers = BannerSerializer(data.get("results"), many=True)
    # data["results"] = serializers.data
    return data


def create_banner(data):
    banner = Banner.objects.create(**data)
    # serializers = BannerSerializer(banner)
    # return serializers.data
    return banner


def update_banner(pk, data):
    try:
        banner = Banner.objects.filter(is_deleted=False).get(id=pk)
        data.pop("image")
        serializers = BannerSerializer(banner, data)
        if serializers.is_valid(raise_exception=True):
            kwargs = {}
            if data.get("area", {}):
                kwargs["area_id"] = data.get("area").get("id")
            serializers.save(**kwargs)
            # return serializers.data
            return banner
    except Banner.DoesNotExist:
        raise ValidationError(detail=BANNER_DOES_NOT_EXIST)


def get_banner(pk):
    try:
        banner = Banner.objects.filter(is_deleted=False).get(id=pk)
        # serializers = BannerSerializer(banner)
        # return serializers.data
        return banner
    except Banner.DoesNotExist:
        raise ValidationError(detail=BANNER_DOES_NOT_EXIST)


def delete_banner(pk):
    try:
        banner = Banner.objects.filter(is_deleted=False).get(pk=pk)
        return banner.delete()
    except Banner.DoesNotExist:
        raise ValidationError(detail=BANNER_DOES_NOT_EXIST)


def upload_image(pk, image_data):
    try:
        banner = Banner.objects.filter(is_deleted=False).get(id=pk)
        banner.image_data = image_data
        banner.save()
        # serializers = BannerSerializer(banner)
        # return serializers.data
        return banner
    except Banner.DoesNotExist:
        raise ValidationError(detail=BANNER_DOES_NOT_EXIST)
