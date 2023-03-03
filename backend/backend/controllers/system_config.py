from rest_framework.response import Response
from rest_framework import status
from ..serializers.system_config import SystemConfigSerializers
from oauth2_provider.decorators import protected_resource
from ..gateways import system_config as system_config_gateway


def list_system_config():
    system_config = system_config_gateway.list_system_config()
    return system_config


def create_system_config(data):
    if "id" in data:
        data.pop("id")
    serializers = SystemConfigSerializers(data=data)
    if serializers.is_valid():
        system_config = system_config_gateway.create_system_config(data)
        return system_config
    # TODO:
    # Raise error in this case
    return serializers.errors


def get_system_config(pk):
    system_config = system_config_gateway.get_system_config(pk)
    return system_config


def update_system_config(pk, data):
    if "id" in data:
        data.pop("id")
    system_config = system_config_gateway.update_system_config(pk, data)
    return system_config


def delete_system_config(pk):
    system_config = system_config_gateway.delete_system_config(pk)
    return system_config
