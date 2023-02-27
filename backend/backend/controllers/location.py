from rest_framework.response import Response
from rest_framework import status
from ..models.location import Location
from ..serializers.location import LocationSerializers
from oauth2_provider.decorators import protected_resource
from ..gateways import location as location_gateway
from ..gateways import state as state_gateway


def list_location():
    location = location_gateway.list_location()
    return location


def create_location(data):
    if "id" in data:
        data.pop("id")
    # data["state"] = state_gateway.get_state(data.get("state").get("id"))
    serializers = LocationSerializers(data=data)
    if serializers.is_valid():
        if data.get("state").get("id"):
            state = data.pop("state")
            data["state_id"] = state.get("id")
        location = location_gateway.create_location(data)
        return location
    # TODO:
    # Raise error in this case
    return serializers.errors


def get_location(pk):
    location = location_gateway.get_location(pk)
    print(location)
    return location


def update_location(pk, data):
    if "id" in data:
        data.pop("id")
    location = location_gateway.update_location(pk, data)
    return location


def delete_location(pk):
    location = location_gateway.delete_location(pk)
    return location

