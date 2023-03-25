from rest_framework.exceptions import ValidationError
from ..models.system_config import SystemConfig
from ..serializers.system_config import SystemConfigSerializer
from ..constants import SYSTEM_CONFIG_DOES_NOT_EXIST


def list_system_config(keys=None, is_active=None):
    system_config = SystemConfig.objects.all().filter(is_deleted=False)
    if keys:
        system_config = system_config.filter(key__in=keys)
    if is_active is not None:
        system_config = system_config.filter(is_active=is_active)
    serializers = SystemConfigSerializer(system_config, many=True)
    return serializers.data


def create_system_config(data):
    system_config = SystemConfig.objects.create(**data)
    serializers = SystemConfigSerializer(system_config)
    return serializers.data


def update_system_config(pk, data):
    try:
        system_config = SystemConfig.objects.filter(is_deleted=False).get(
            id=pk
        )
        serializers = SystemConfigSerializer(system_config, data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return serializers.data
    except SystemConfig.DoesNotExist:
        raise ValidationError(
            detail=SYSTEM_CONFIG_DOES_NOT_EXIST
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
        serializers = SystemConfigSerializer(system_config)
        return serializers.data
    except SystemConfig.DoesNotExist:
        raise ValidationError(
            detail=SYSTEM_CONFIG_DOES_NOT_EXIST
        )


def delete_system_config(pk):
    try:
        system_config = SystemConfig.objects.filter(is_deleted=False).get(
            pk=pk
        )
        return system_config.delete()
    except SystemConfig.DoesNotExist:
        raise ValidationError(
            detail=SYSTEM_CONFIG_DOES_NOT_EXIST
        )
