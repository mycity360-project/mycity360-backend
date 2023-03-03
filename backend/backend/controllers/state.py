from rest_framework.response import Response
from rest_framework import status
from ..models.state import State
from ..serializers.state import StateSerializers
from oauth2_provider.decorators import protected_resource
from ..gateways import state as state_gateway


def list_state():
    state = state_gateway.list_state()
    return state


def create_state(data):
    if "id" in data:
        data.pop("id")
    serializers = StateSerializers(data=data)
    if serializers.is_valid():
        state = state_gateway.create_state(data)
        return state
    # TODO:
    # Raise error in this case
    return serializers.errors


def get_state(pk):
    state = state_gateway.get_state(pk)
    return state


def update_state(pk, data):
    if "id" in data:
        data.pop("id")
    state = state_gateway.update_state(pk, data)
    return state


def delete_state(pk):
    state = state_gateway.delete_state(pk)
    return state
