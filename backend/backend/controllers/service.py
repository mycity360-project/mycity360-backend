from rest_framework.exceptions import ValidationError
from ..constants import FILE_REQUIRED
from ..serializers.service import ServiceSerializer
from ..gateways import service as service_gateway
from ..utils.cache import cache
from ..utils.google_api import upload_to_local, delete_image
from ..controllers.image import delete_image


@cache(invalidate=False)
def list_service(is_active=None, ordering=None, search=None):
    service = service_gateway.list_service(
        is_active=is_active, ordering=ordering, search=search
    )
    service = [ServiceSerializer.serialize_data(data) for data in service]
    return service


@cache(invalidate=True)
def create_service(data):
    if "id" in data:
        data.pop("id")
    serializers = ServiceSerializer(data=data)
    if serializers.is_valid(raise_exception=True):
        service = service_gateway.create_service(data)
        return ServiceSerializer.serialize_data(service)


@cache(invalidate=False)
def get_service(pk):
    service = service_gateway.get_service(pk)
    return ServiceSerializer.serialize_data(service)


@cache(invalidate=True)
def update_service(pk, data):
    if "id" in data:
        data.pop("id")
    service = service_gateway.update_service(pk, data)
    return ServiceSerializer.serialize_data(service)


@cache(invalidate=True)
def delete_service(pk):
    service = service_gateway.get_service(pk)
    service = ServiceSerializer.serialize_data(service)
    if service.get("icon"):
        delete_image(service.get("icon"))
    for img in service.get("images"):
        delete_image(pk=img.get("id"))
    service = service_gateway.delete_service(pk)
    return service


@cache(invalidate=True)
def upload_icon(pk, icon):
    if not icon:
        raise ValidationError(detail=FILE_REQUIRED)
    service = service_gateway.get_service(pk)
    if service.icon:
        delete_image(service.icon)
    service = service_gateway.upload_icon(
        pk, upload_to_local(icon, folder="service")
    )
    return ServiceSerializer.serialize_data(service)
