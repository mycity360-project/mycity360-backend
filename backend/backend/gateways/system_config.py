from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from ..models.system_config import SystemConfig
from ..serializers.system_config import SystemConfigSerializers
from oauth2_provider.decorators import protected_resource


def list_system_config(keys=None):
    system_config = SystemConfig.objects.all().filter(is_deleted=False)
    if keys:
        system_config = system_config.filter(key__in=keys)
    serializers = SystemConfigSerializers(system_config, many=True)
    return serializers.data


def create_system_config(data):
    system_config = SystemConfig.objects.create(**data)
    serializers = SystemConfigSerializers(system_config)
    return serializers.data


def update_system_config(pk, data):
    try:
        system_config = SystemConfig.objects.filter(is_deleted=False).get(
            id=pk
        )
        serializers = SystemConfigSerializers(system_config, data)
        if serializers.is_valid():
            serializers.save()
            return serializers.data
    except SystemConfig.DoesNotExist:
        raise ValidationError(
            detail="System Config with this id does not exist"
        )


def get_system_config(pk=None, key=None):
    try:
        kwargs = dict()
        if pk:
            kwargs["pk"] = pk
        if key:
            kwargs["key"] = key
        system_config = SystemConfig.objects.filter(is_deleted=False).get(
            **kwargs
        )
        serializers = SystemConfigSerializers(system_config)
        return serializers.data
    except SystemConfig.DoesNotExist:
        raise ValidationError(
            detail="System Config with this id does not exist"
        )


def delete_system_config(pk):
    try:
        system_config = SystemConfig.objects.filter(is_deleted=False).get(
            pk=pk
        )
        return system_config.delete()
    except SystemConfig.DoesNotExist:
        raise ValidationError(
            detail="System Config with this id does not exist"
        )
