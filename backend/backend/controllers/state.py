from ..serializers.state import StateSerializer
from ..gateways import state as state_gateway


def list_state(is_active=None, ordering=None):
    state = state_gateway.list_state(is_active=is_active, ordering=ordering)
    return state


def create_state(data):
    if "id" in data:
        data.pop("id")
    serializers = StateSerializer(data=data)
    if serializers.is_valid(raise_exception=True):
        state = state_gateway.create_state(data)
        return state


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
