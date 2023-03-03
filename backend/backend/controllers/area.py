from rest_framework.response import Response
from rest_framework import status
from ..models.area import Area
from ..serializers.area import AreaSerializers
from oauth2_provider.decorators import protected_resource
from ..gateways import area as area_gateway


def list_area():
    area = area_gateway.list_area()
    return area


def create_area(data):
    if "id" in data:
        data.pop("id")
    serializers = AreaSerializers(data=data)
    if serializers.is_valid():
        location = data.pop("location")
        data["location_id"] = location.get("id")
        area = area_gateway.create_area(data)
        return area
    # TODO:
    # Raise error in this case
    return serializers.errors


def get_area(pk):
    area = area_gateway.get_area(pk)
    return area


def update_area(pk, data):
    if "id" in data:
        data.pop("id")
    area = area_gateway.update_area(pk, data)
    return area


def delete_area(pk):
    area = area_gateway.delete_area(pk)
    return area
