from ..serializers.service import ServiceSerializer
from ..gateways import service as service_gateway


def list_service(is_active=None, ordering=None):
    service = service_gateway.list_service(
        is_active=is_active, ordering=ordering
    )
    return service


def create_service(data):
    if "id" in data:
        data.pop("id")
    serializers = ServiceSerializer(data=data)
    if serializers.is_valid(raise_exception=True):
        service = service_gateway.create_service(data)
        return service


def get_service(pk):
    service = service_gateway.get_service(pk)
    return service


def update_service(pk, data):
    if "id" in data:
        data.pop("id")
    service = service_gateway.update_service(pk, data)
    return service


def delete_service(pk):
    service = service_gateway.delete_service(pk)
    return service
