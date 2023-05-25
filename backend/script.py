import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from backend.models.category import Category
from backend.models.banner import Banner
from backend.models.service import Service
from backend import constants
import traceback

from uuid import uuid4
import requests


def upload_to_local(
    file,
    ext,
    folder=None,
):
    """Insert new file.
    Returns : Id's of the file uploaded
    """
    try:

        base_folder = f"{constants.MEDIA_ROOT}"
        if folder:
            base_folder = f"{constants.MEDIA_ROOT}{folder}/"
        if not os.path.exists(base_folder):
            os.mkdir(base_folder)
        file_name = f"{uuid4()}.png"
        img_save_path = f"{base_folder}{file_name}"
        with open(img_save_path, "wb+") as f:
            f.write(file)
        path = f"{constants.SERVER_BASE_URL}{folder}/{file_name}"
        return path
    except:
        print(traceback.format_exc())


#
# category = Category.objects.all()
# for cat in category:
#     if cat.icon:
#         try:
#             response = requests.get(cat.icon)
#             path = upload_to_local(
#                 response.content,
#                 ext=f'.{cat.icon.split(".")[-1]}',
#                 folder="category",
#             )
#             c = Category.objects.get(id=cat.id)
#             c.icon = path
#             c.save()
#         except Exception as e:
#             print("Category")
#             print(e)

# banner = Banner.objects.all()
# for cat in banner:
#     if cat.image:
#         try:
#             response = requests.get(cat.image)
#             path = upload_to_local(
#                 response.content,
#                 ext=f'.{cat.image.split(".")[-1]}',
#                 folder="banner",
#             )
#             c = Banner.objects.get(id=cat.id)
#             c.image = path
#             c.save()
#         except Exception as e:
#             print("Banner")
#             print(e)

service = Service.objects.all()
for cat in service:
    if cat.icon:
        try:
            print(cat.id)
            response = requests.get(cat.icon)
            print("=============")
            print(response)
            path = upload_to_local(
                response.content,
                ext=f'.{cat.icon.split(".")[-1]}',
                folder="service",
            )
            c = Service.objects.get(id=cat.id)
            print(c.icon)
            c.icon = path
            c.save()
        except Exception as e:
            print("Service")
            print(e)
