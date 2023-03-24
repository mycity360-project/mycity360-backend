from rest_framework.exceptions import ValidationError
from ..models.state import State
from ..serializers.state import StateSerializer


def list_state(is_active=None):
    state = State.objects.all().filter(is_deleted=False)
    if is_active is not None:
        state = state.filter(is_active=is_active)
    serializers = StateSerializer(state, many=True)
    return serializers.data


def create_state(data):
    state = State.objects.create(**data)
    serializers = StateSerializer(state)
    return serializers.data


def update_state(pk, data):
    try:
        state = State.objects.filter(is_deleted=False).get(id=pk)
        serializers = StateSerializer(state, data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return serializers.data
    except State.DoesNotExist:
        raise ValidationError(detail="State with this id does not exist")


def get_state(pk):
    try:
        state = State.objects.filter(is_deleted=False).get(id=pk)
        serializers = StateSerializer(state)
        return serializers.data
    except State.DoesNotExist:
        raise ValidationError(detail="State with this id does not exist")


def delete_state(pk):
    try:
        state = State.objects.filter(is_deleted=False).get(pk=pk)
        return state.delete()
    except State.DoesNotExist:
        raise ValidationError(detail="State with this id does not exist")
