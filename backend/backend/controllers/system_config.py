from rest_framework.response import Response
from rest_framework import status
from ..models.state import State
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
        state = system_config_gateway.create_system_config(data)
        return state
    # TODO:
    # Raise error in this case
    return serializers.errors


def get_system_config(pk):
    state = system_config_gateway.get_system_config(pk)
    print(state)
    return state


def update_system_config(pk, data):
    if "id" in data:
        data.pop("id")
    state = system_config_gateway.update_system_config(pk, data)
    return state


def delete_system_config(pk):
    state = system_config_gateway.delete_system_config(pk)
    return state

