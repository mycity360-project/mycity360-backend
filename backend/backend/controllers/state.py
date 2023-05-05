from ..serializers.state import StateSerializer
from ..gateways import state as state_gateway
from ..utils.cache import cache

@cache(invalidate=False)
def list_state(is_active=None, ordering=None):
    state = state_gateway.list_state(is_active=is_active, ordering=ordering)
    state = [StateSerializer.serialize_data(data) for data in state]
    return state

@cache(invalidate=True)
def create_state(data):
    if "id" in data:
        data.pop("id")
    serializers = StateSerializer(data=data)
    if serializers.is_valid(raise_exception=True):
        state = state_gateway.create_state(data)
        return StateSerializer.serialize_data(state)

@cache(invalidate=False)
def get_state(pk):
    state = state_gateway.get_state(pk)
    return StateSerializer.serialize_data(state)

@cache(invalidate=True)
def update_state(pk, data):
    if "id" in data:
        data.pop("id")
    state = state_gateway.update_state(pk, data)
    return StateSerializer.serialize_data(state)

@cache(invalidate=True)
def delete_state(pk):
    state = state_gateway.delete_state(pk)
    return StateSerializer.serialize_data(state)
