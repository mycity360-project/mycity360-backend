from rest_framework.exceptions import ValidationError
from ..constants import FILE_REQUIRED
from ..serializers.image import ImageSerializer
from ..gateways import image as image_gateway
from ..utils.google_api import upload_basic


def upload_image(image):
    if not image:
        raise ValidationError(detail=FILE_REQUIRED)
    image = image_gateway.create_image(data=dict(url=upload_basic(image)))
    return ImageSerializer.serialize_data(image)
