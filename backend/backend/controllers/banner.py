from ..serializers.banner import BannerSerializer
from rest_framework.exceptions import ValidationError
from ..constants import FILE_REQUIRED
from ..gateways import banner as banner_gateway
from ..utils.cache import cache
from ..utils.google_api import upload_to_local, delete_image


@cache(invalidate=False)
def list_banner(
    is_active=True,
    area_id=None,
    page=1,
    page_size=10,
    ordering=None,
    search=None,
):
    banner = banner_gateway.list_banner(
        is_active=is_active,
        area_id=area_id,
        page=page,
        page_size=page_size,
        ordering=ordering,
        search=search,
    )
    banner["results"] = [
        BannerSerializer.serialize_data(data) for data in banner.get("results")
    ]
    return banner


@cache(invalidate=True)
def create_banner(data):
    if "id" in data:
        data.pop("id")
    if "image" in data and not data.get("image"):
        data.pop("image")
    # TODO: Add support to save data and upload image in this api
    serializers = BannerSerializer(data=data)
    if serializers.is_valid(raise_exception=True):
        area = data.pop("area")
        data["area_id"] = area.get("id")
        banner = banner_gateway.create_banner(data)
        return BannerSerializer.serialize_data(banner)


@cache(invalidate=False)
def get_banner(pk):
    banner = banner_gateway.get_banner(pk)
    return BannerSerializer.serialize_data(banner)


@cache(invalidate=True)
def update_banner(pk, data):
    if "id" in data:
        data.pop("id")
    banner = banner_gateway.update_banner(pk, data)
    return BannerSerializer.serialize_data(banner)


@cache(invalidate=True)
def delete_banner(pk):
    banner = banner_gateway.get_banner(pk)
    if banner.image:
        delete_image(banner.image)
    banner = banner_gateway.delete_banner(pk)
    return banner


@cache(invalidate=True)
def upload_image(pk, image):
    if not image:
        raise ValidationError(detail=FILE_REQUIRED)
    banner = banner_gateway.get_banner(pk)
    if banner.image:
        delete_image(banner.image)
    banner = banner_gateway.upload_image(pk, image)
    return BannerSerializer.serialize_data(banner)
