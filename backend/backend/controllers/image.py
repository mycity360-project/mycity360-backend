from rest_framework.exceptions import ValidationError
from ..constants import FILE_REQUIRED
from ..serializers.image import ImageSerializer
from ..gateways import image as image_gateway
from ..utils.google_api import upload_to_local


def upload_image(image):
    if not image:
        raise ValidationError(detail=FILE_REQUIRED)
    image = image_gateway.create_image(
        data=dict(image=upload_to_local(image, folder="image"))
    )
    return ImageSerializer.serialize_data(image)


def upload_image_v2(image):
    if not image:
        raise ValidationError(detail=FILE_REQUIRED)
    image = image_gateway.create_image(
        data=dict(image=upload_to_local(image, folder="image"))
    )
    return ImageSerializer.serialize_data(image)


def delete_image(pk):
    image = image_gateway.get_image(pk)
    if image.image:
        delete_image(image.image)
    image = image_gateway.delete_image(pk)
    return image
