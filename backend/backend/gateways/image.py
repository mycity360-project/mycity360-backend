from rest_framework.exceptions import ValidationError
from ..models.image import Image
from ..serializers.image import ImageSerializer
from ..constants import IMAGE_DOES_NOT_EXIST


def list_image(is_active=None):
    image = Image.objects.all().filter(is_deleted=False)
    if is_active is not None:
        image = image.filter(is_active=is_active)
    serializers = ImageSerializer(image, many=True)
    return serializers.data


def create_image(data):
    image = Image.objects.create(**data)
    serializers = ImageSerializer(image)
    return serializers.data


def update_image(pk, data):
    try:
        image = Image.objects.filter(is_deleted=False).get(id=pk)
        serializers = ImageSerializer(image, data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return serializers.data
    except Image.DoesNotExist:
        raise ValidationError(detail=IMAGE_DOES_NOT_EXIST)


def get_image(pk):
    try:
        image = Image.objects.filter(is_deleted=False).get(id=pk)
        serializers = ImageSerializer(image)
        return serializers.data
    except Image.DoesNotExist:
        raise ValidationError(detail=IMAGE_DOES_NOT_EXIST)


def delete_image(pk):
    try:
        image = Image.objects.filter(is_deleted=False).get(pk=pk)
        return image.delete()
    except Image.DoesNotExist:
        raise ValidationError(detail=IMAGE_DOES_NOT_EXIST)
