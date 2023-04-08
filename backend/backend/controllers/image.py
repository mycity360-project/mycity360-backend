from ..serializers.image import ImageSerializer
from ..gateways import image as image_gateway


def upload_image(image):
    image = image_gateway.create_image(data=dict(image=image))
    return ImageSerializer.serialize_data(image)
