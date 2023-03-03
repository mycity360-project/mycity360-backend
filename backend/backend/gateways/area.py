from rest_framework.response import Response
from rest_framework import status
from ..models.area import Area
from ..serializers.area import AreaSerializers
from oauth2_provider.decorators import protected_resource


def list_area():
    area = Area.objects.all().filter(is_deleted=False)
    serializers = AreaSerializers(area, many=True)
    return serializers.data


def create_area(data):
    area = Area.objects.create(**data)
    serializers = AreaSerializers(area)
    return serializers.data


def update_area(pk, data):
    try:
        area = Area.objects.filter(is_deleted=False).get(id=pk)
        serializers = AreaSerializers(area, data)
        if serializers.is_valid():
            serializers.save(location_id=data.get("location").get("id"))
            return serializers.data
    except Area.DoesNotExist:
        # TODO:
        # Raise error
        return {
            "id": ["area with this id does not exist"]
        }, status.HTTP_404_NOT_FOUND


def get_area(pk):
    try:
        area = Area.objects.filter(is_deleted=False).get(id=pk)
        serializers = AreaSerializers(area)
        return serializers.data
    except Area.DoesNotExist:
        # TODO:
        # Raise error
        return {
            "id": ["area with this id does not exist"]
        }, status.HTTP_404_NOT_FOUND


def delete_area(pk):
    try:
        area = Area.objects.filter(is_deleted=False).get(pk=pk)
        return area.delete()
    except Area.DoesNotExist:
        # TODO:
        # Raise error
        return {
            "id": ["area with this id does not exist"]
        }, status.HTTP_404_NOT_FOUND
