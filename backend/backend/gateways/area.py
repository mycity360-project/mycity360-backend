from rest_framework.exceptions import ValidationError
from ..models.area import Area
from ..serializers.area import AreaSerializer
from ..constants import AREA_DOES_NOT_EXIST


def list_area(is_active=None, location_id=None):
    area = Area.objects.all().filter(is_deleted=False)
    if is_active is not None:
        area = area.filter(is_active=is_active)
    if location_id is not None:
        area = area.filter(location_id=location_id)
    serializers = AreaSerializer(area, many=True)
    return serializers.data


def create_area(data):
    area = Area.objects.create(**data)
    serializers = AreaSerializer(area)
    return serializers.data


def update_area(pk, data):
    try:
        area = Area.objects.filter(is_deleted=False).get(id=pk)
        serializers = AreaSerializer(area, data)
        if serializers.is_valid(raise_exception=True):
            serializers.save(location_id=data.get("location").get("id"))
            return serializers.data
    except Area.DoesNotExist:
        raise ValidationError(detail=AREA_DOES_NOT_EXIST)


def get_area(pk):
    try:
        area = Area.objects.filter(is_deleted=False).get(id=pk)
        serializers = AreaSerializer(area)
        return serializers.data
    except Area.DoesNotExist:
        raise ValidationError(detail=AREA_DOES_NOT_EXIST)


def delete_area(pk):
    try:
        area = Area.objects.filter(is_deleted=False).get(pk=pk)
        return area.delete()
    except Area.DoesNotExist:
        raise ValidationError(detail=AREA_DOES_NOT_EXIST)
