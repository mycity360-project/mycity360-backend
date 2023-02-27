from rest_framework.response import Response
from rest_framework import status
from ..models.state import State
from ..serializers.state import StateSerializers
from oauth2_provider.decorators import protected_resource


def list_state():
    state = State.objects.all().filter(is_deleted=False)
    serializers = StateSerializers(state, many=True)
    return serializers.data


def create_state(data):
    state = State.objects.create(**data)
    serializers = StateSerializers(state)
    return serializers.data


def update_state(pk, data):
    try:
        state = State.objects.filter(is_deleted=False).get(id=pk)
        serializers = StateSerializers(state, data)
        if serializers.is_valid():
            serializers.save()
            return serializers.data
    except State.DoesNotExist:
        # TODO:
        # Raise error
        return {
                   "id": ["state with this id does not exist"]
               }, status.HTTP_404_NOT_FOUND


def get_state(pk):
    try:
        state = State.objects.filter(is_deleted=False).get(id=pk)
        serializers = StateSerializers(state)
        return serializers.data
    except State.DoesNotExist:
        # TODO:
        # Raise error
        return {
                   "id": ["state with this id does not exist"]
               }, status.HTTP_404_NOT_FOUND


def delete_state(pk):
    try:
        state = State.objects.filter(is_deleted=False).get(pk=pk)
        return state.delete()
    except State.DoesNotExist:
        # TODO:
        # Raise error
        return {
                   "id": ["state with this id does not exist"]
               }, status.HTTP_404_NOT_FOUND