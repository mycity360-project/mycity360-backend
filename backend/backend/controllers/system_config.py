from ..serializers.system_config import SystemConfigSerializer
from ..gateways import system_config as system_config_gateway


def list_system_config(is_active=None, key=None, ordering=None, search=None):
    system_config = system_config_gateway.list_system_config(
        is_active=is_active, key=key, ordering=ordering, search=search
    )
    system_config = [
        SystemConfigSerializer.serialize_data(data) for data in system_config
    ]
    return system_config


def create_system_config(data):
    if "id" in data:
        data.pop("id")
    serializers = SystemConfigSerializer(data=data)
    if serializers.is_valid(raise_exception=True):
        system_config = system_config_gateway.create_system_config(data)
        return SystemConfigSerializer.serialize_data(system_config)


def get_system_config(pk):
    system_config = system_config_gateway.get_system_config(pk)
    return SystemConfigSerializer.serialize_data(system_config)


def update_system_config(pk, data):
    if "id" in data:
        data.pop("id")
    system_config = system_config_gateway.update_system_config(pk, data)
    return SystemConfigSerializer.serialize_data(system_config)


def delete_system_config(pk):
    system_config = system_config_gateway.delete_system_config(pk)
    return SystemConfigSerializer.serialize_data(system_config)
