from ..serializers.location import LocationSerializer
from ..gateways import location as location_gateway


def list_location(is_active=None, state_id=None, ordering=None):
    location = location_gateway.list_location(
        is_active=is_active, state_id=state_id, ordering=ordering
    )
    location = [LocationSerializer.serialize_data(data) for data in location]
    return location


def create_location(data):
    if "id" in data:
        data.pop("id")
    serializers = LocationSerializer(data=data)
    if serializers.is_valid(raise_exception=True):
        if data.get("state").get("id"):
            state = data.pop("state")
            data["state_id"] = state.get("id")
        location = location_gateway.create_location(data)
        return LocationSerializer.serialize_data(location)


def get_location(pk):
    location = location_gateway.get_location(pk)
    return LocationSerializer.serialize_data(location)


def update_location(pk, data):
    if "id" in data:
        data.pop("id")
    location = location_gateway.update_location(pk, data)
    return LocationSerializer.serialize_data(location)


def delete_location(pk):
    location = location_gateway.delete_location(pk)
    return LocationSerializer.serialize_data(location)
