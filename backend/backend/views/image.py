from rest_framework import status
from rest_framework.decorators import (
    api_view,
)
from ..controllers import image as image_controller
from ..utils.views import response_handler


@api_view(["POST"])
@response_handler()
def image_upload(request):
    response = image_controller.upload_image(
        request.FILES.get('file')
    )
    return response, status.HTTP_200_OK
