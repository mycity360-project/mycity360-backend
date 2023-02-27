from rest_framework.response import Response
from rest_framework import status
from ..models.system_config import SystemConfig
from ..serializers.system_config import SystemConfigSerializers
from oauth2_provider.decorators import protected_resource


def list_system_config():
    system_config = SystemConfig.objects.all().filter(is_deleted=False)
    serializers = SystemConfigSerializers(system_config, many=True)
    return serializers.data


def create_system_config(data):
    system_config = SystemConfig.objects.create(**data)
    serializers = SystemConfigSerializers(system_config)
    return serializers.data


def update_system_config(pk, data):
    try:
        system_config = SystemConfig.objects.filter(is_deleted=False).get(id=pk)
        serializers = SystemConfigSerializers(system_config, data)
        if serializers.is_valid():
            serializers.save()
            return serializers.data
    except SystemConfig.DoesNotExist:
        # TODO:
        # Raise error
        return {
                   "id": ["system_config with this id does not exist"]
               }, status.HTTP_404_NOT_FOUND


def get_system_config(pk):
    try:
        system_config = SystemConfig.objects.filter(is_deleted=False).get(id=pk)
        serializers = SystemConfigSerializers(system_config)
        return serializers.data
    except SystemConfig.DoesNotExist:
        # TODO:
        # Raise error
        return {
                   "id": ["system_config with this id does not exist"]
               }, status.HTTP_404_NOT_FOUND


def delete_system_config(pk):
    try:
        system_config = SystemConfig.objects.filter(is_deleted=False).get(pk=pk)
        return system_config.delete()
    except SystemConfig.DoesNotExist:
        # TODO:
        # Raise error
        return {
                   "id": ["system_config with this id does not exist"]
               }, status.HTTP_404_NOT_FOUND