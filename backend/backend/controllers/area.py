from ..serializers.area import AreaSerializer
from ..gateways import area as area_gateway


def list_area(is_active=None, location_id=None, ordering=None):
    area = area_gateway.list_area(
        is_active=is_active, location_id=location_id, ordering=ordering
    )
    area = [AreaSerializer.serialize_data(data) for data in area]
    return area


def create_area(data):
    if "id" in data:
        data.pop("id")
    serializers = AreaSerializer(data=data)
    if serializers.is_valid(raise_exception=True):
        location = data.pop("location")
        data["location_id"] = location.get("id")
        area = area_gateway.create_area(data)
        return AreaSerializer.serialize_data(area)


def get_area(pk):
    area = area_gateway.get_area(pk)
    return AreaSerializer.serialize_data(area)


def update_area(pk, data):
    if "id" in data:
        data.pop("id")
    area = area_gateway.update_area(pk, data)
    return AreaSerializer.serialize_data(area)


def delete_area(pk):
    area = area_gateway.delete_area(pk)
    return AreaSerializer.serialize_data(area)
