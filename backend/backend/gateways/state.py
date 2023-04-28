from rest_framework.exceptions import ValidationError
from ..models.state import State
from ..serializers.state import StateSerializer
from ..constants import STATE_DOES_NOT_EXIST


def list_state(is_active=None, ordering=None):
    state = State.objects.all().filter(is_deleted=False)
    if is_active is not None:
        state = state.filter(is_active=is_active)
    if not ordering:
        ordering = "-pk"
    state = state.order_by(ordering)
    # serializers = StateSerializer(state, many=True)
    # return serializers.data
    return state


def create_state(data):
    state = State.objects.create(**data)
    # serializers = StateSerializer(state)
    # return serializers.data
    return state


def update_state(pk, data):
    try:
        state = State.objects.filter(is_deleted=False).get(id=pk)
        serializers = StateSerializer(state, data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            # return serializers.data
            return state
    except State.DoesNotExist:
        raise ValidationError(detail=STATE_DOES_NOT_EXIST)


def get_state(pk):
    try:
        state = State.objects.filter(is_deleted=False).get(id=pk)
        # serializers = StateSerializer(state)
        # return serializers.data
        return state
    except State.DoesNotExist:
        raise ValidationError(detail=STATE_DOES_NOT_EXIST)


def delete_state(pk):
    try:
        state = State.objects.filter(is_deleted=False).get(pk=pk)
        return state.delete()
    except State.DoesNotExist:
        raise ValidationError(detail=STATE_DOES_NOT_EXIST)
