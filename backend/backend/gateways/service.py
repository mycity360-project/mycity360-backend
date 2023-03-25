from rest_framework.exceptions import ValidationError
from ..models.service import Service
from ..serializers.service import ServiceSerializer
from ..constants import SERVICE_DOES_NOT_EXIST


def list_service(is_active=None):
    service = Service.objects.all().filter(is_deleted=False)
    if is_active is not None:
        service = service.filter(is_active=is_active)
    serializers = ServiceSerializer(service, many=True)
    return serializers.data


def create_service(data):
    images = data.pop("images")
    service = Service.objects.create(**data)
    for image in images:
        service.images.add(image)
    service.save()
    serializers = ServiceSerializer(service)
    return serializers.data


def update_service(pk, data):
    try:
        service = Service.objects.filter(is_deleted=False).get(id=pk)
        serializers = ServiceSerializer(service, data)
        for image in data.get("images"):
            service.images.add(image)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return serializers.data
    except Service.DoesNotExist:
        raise ValidationError(detail=SERVICE_DOES_NOT_EXIST)


def get_service(pk):
    try:
        service = Service.objects.filter(is_deleted=False).get(id=pk)
        serializers = ServiceSerializer(service)
        return serializers.data
    except Service.DoesNotExist:
        raise ValidationError(detail=SERVICE_DOES_NOT_EXIST)


def delete_service(pk):
    try:
        service = Service.objects.filter(is_deleted=False).get(pk=pk)
        return service.delete()
    except Service.DoesNotExist:
        raise ValidationError(detail=SERVICE_DOES_NOT_EXIST)
