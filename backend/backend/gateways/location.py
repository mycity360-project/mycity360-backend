from rest_framework.exceptions import ValidationError
from ..models.location import Location
from ..serializers.location import LocationSerializer
from ..constants import LOCATION_DOES_NOT_EXIST


def list_location(is_active=None):
    location = Location.objects.all().filter(is_deleted=False)
    if is_active is not None:
        location = location.filter(is_active=is_active)
    serializers = LocationSerializer(location, many=True)
    return serializers.data


def create_location(data):
    location = Location.objects.create(**data)
    serializers = LocationSerializer(location)
    return serializers.data


def update_location(pk, data):
    try:
        location = Location.objects.filter(is_deleted=False).get(id=pk)
        serializers = LocationSerializer(location, data)
        if serializers.is_valid(raise_exception=True):
            serializers.save(state_id=data.get("state").get("id"))
            return serializers.data
    except Location.DoesNotExist:
        raise ValidationError(detail=LOCATION_DOES_NOT_EXIST)


def get_location(pk):
    try:
        location = Location.objects.filter(is_deleted=False).get(id=pk)
        serializers = LocationSerializer(location)
        return serializers.data
    except Location.DoesNotExist:
        raise ValidationError(detail=LOCATION_DOES_NOT_EXIST)


def delete_location(pk):
    try:
        location = Location.objects.filter(is_deleted=False).get(pk=pk)
        return location.delete()
    except Location.DoesNotExist:
        raise ValidationError(detail=LOCATION_DOES_NOT_EXIST)
