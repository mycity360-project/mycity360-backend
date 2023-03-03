from rest_framework.response import Response
from rest_framework import status
from ..models.location import Location
from ..serializers.location import LocationSerializers


def list_location():
    location = Location.objects.all().filter(is_deleted=False)
    serializers = LocationSerializers(location, many=True)
    return serializers.data


def create_location(data):
    location = Location.objects.create(**data)
    serializers = LocationSerializers(location)
    return serializers.data


def update_location(pk, data):
    try:
        location = Location.objects.filter(is_deleted=False).get(id=pk)
        serializers = LocationSerializers(location, data)
        if serializers.is_valid():
            serializers.save(state_id=data.get("state").get("id"))
            return serializers.data
    except Location.DoesNotExist:
        # TODO:
        # Raise error
        return {
            "id": ["location with this id does not exist"]
        }, status.HTTP_404_NOT_FOUND


def get_location(pk):
    try:
        location = Location.objects.filter(is_deleted=False).get(id=pk)
        serializers = LocationSerializers(location)
        return serializers.data
    except Location.DoesNotExist:
        # TODO:
        # Raise error
        return {
            "id": ["location with this id does not exist"]
        }, status.HTTP_404_NOT_FOUND


def delete_location(pk):
    try:
        location = Location.objects.filter(is_deleted=False).get(pk=pk)
        return location.delete()
    except Location.DoesNotExist:
        # TODO:
        # Raise error
        return {
            "id": ["location with this id does not exist"]
        }, status.HTTP_404_NOT_FOUND
