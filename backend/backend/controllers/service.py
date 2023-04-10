from rest_framework.exceptions import ValidationError
from ..constants import FILE_REQUIRED
from ..serializers.service import ServiceSerializer
from ..gateways import service as service_gateway


def list_service(is_active=None, ordering=None):
    service = service_gateway.list_service(
        is_active=is_active, ordering=ordering
    )
    service = [ServiceSerializer.serialize_data(data) for data in service]
    return service


def create_service(data):
    if "id" in data:
        data.pop("id")
    serializers = ServiceSerializer(data=data)
    if serializers.is_valid(raise_exception=True):
        service = service_gateway.create_service(data)
        return ServiceSerializer.serialize_data(service)


def get_service(pk):
    service = service_gateway.get_service(pk)
    return ServiceSerializer.serialize_data(service)


def update_service(pk, data):
    if "id" in data:
        data.pop("id")
    service = service_gateway.update_service(pk, data)
    return ServiceSerializer.serialize_data(service)


def delete_service(pk):
    service = service_gateway.delete_service(pk)
    return service


def upload_icon(pk, icon):
    if not icon:
        raise ValidationError(detail=FILE_REQUIRED)
    service = service_gateway.upload_icon(pk, icon)
    return ServiceSerializer.serialize_data(service)
