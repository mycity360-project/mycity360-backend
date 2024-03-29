from rest_framework.exceptions import ValidationError
from ..models.service import Service
from ..serializers.service import ServiceSerializer
from ..constants import SERVICE_DOES_NOT_EXIST


def list_service(is_active=True, ordering=None, search=None):
    service = Service.objects.all().filter(is_deleted=False)
    if is_active is not None:
        service = service.filter(is_active=is_active)
    if search:
        service = service.filter(name__icontains=search)
    if not ordering:
        ordering = "sequence"
    service = service.order_by(ordering)
    # serializers = ServiceSerializer(service, many=True)
    # return serializers.data
    return service


def create_service(data):
    images = data.pop("images")
    service = Service.objects.create(**data)
    for image in images:
        service.images.add(image.get("id"))
    service.save()
    # serializers = ServiceSerializer(service)
    # return serializers.data
    return service


def update_service(pk, data):
    try:
        service = Service.objects.filter(is_deleted=False).get(id=pk)
        if "icon" in data:
            data.pop("icon")
        service.images.clear()
        for image in data.get("images"):
            service.images.add(image.get("id"))
        serializers = ServiceSerializer(service, data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            # return serializers.data
            return service
    except Service.DoesNotExist:
        raise ValidationError(detail=SERVICE_DOES_NOT_EXIST)


def get_service(pk):
    try:
        service = Service.objects.filter(is_deleted=False, is_active=True).get(
            id=pk
        )
        # serializers = ServiceSerializer(service)
        # return serializers.data
        return service
    except Service.DoesNotExist:
        raise ValidationError(detail=SERVICE_DOES_NOT_EXIST)


def delete_service(pk):
    try:
        service = Service.objects.filter(is_deleted=False).get(pk=pk)
        return service.delete()
    except Service.DoesNotExist:
        raise ValidationError(detail=SERVICE_DOES_NOT_EXIST)


def upload_icon(pk, icon_data):
    try:
        service = Service.objects.filter(is_deleted=False).get(id=pk)
        service.icon_data = icon_data
        service.save()
        # serializers = ServiceSerializer(service)
        # return serializers.data
        return service
    except Service.DoesNotExist:
        raise ValidationError(detail=SERVICE_DOES_NOT_EXIST)
