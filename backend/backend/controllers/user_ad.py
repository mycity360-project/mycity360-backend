import string
import random
from ..serializers.user_ad import UserAdSerializer
from ..gateways import user_ad as user_ad_gateway
from ..controllers import category as category_controller
from ..controllers.image import delete_image


def list_user_ad(
    is_active=None,
    is_featured=None,
    category_id=None,
    user_id=None,
    area_id=None,
    location_id=None,
    page=1,
    page_size=10,
    ordering=None,
    search=None,
):
    user_ads = user_ad_gateway.list_user_ad(
        is_active=is_active,
        is_featured=is_featured,
        category_id=category_id,
        user_id=user_id,
        area_id=area_id,
        location_id=location_id,
        page=page,
        page_size=page_size,
        ordering=ordering,
        search=search,
    )
    user_ads["results"] = [
        UserAdSerializer.serialize_data(user_ad)
        for user_ad in user_ads.get("results")
    ]
    return user_ads


def create_user_ad(data):
    if "id" in data:
        data.pop("id")
    data["code"] = "".join(
        random.choices(string.ascii_uppercase + string.digits, k=10)
    )
    serializers = UserAdSerializer(data=data)
    if serializers.is_valid(raise_exception=True):
        category = data.pop("category")
        if category:
            data["category_id"] = category.get("id")
            category = category_controller.get_category(category.get("id"))
        user = data.pop("user")
        if user:
            data["user_id"] = user.get("id")
        area = data.pop("area")
        if area:
            data["area_id"] = area.get("id")
        tags = []
        if data.get("tags"):
            tags = data.get("tags")
        tags.append(data.get("code"))
        if data.get("name"):
            tags.extend(data.get("name").split(" "))
        if data.get("description"):
            tags.extend(data.get("description").split(" "))
        if category and category.get("name"):
            tags.extend(category.get("name").split(" "))
        tags = list(
            filter(
                lambda x: True if x and x != " " and x != "," else False, tags
            )
        )
        tags = [i.replace(",", "") for i in tags]
        data["tags"] = tags
        user_ad = user_ad_gateway.create_user_ad(data)
        return UserAdSerializer.serialize_data(user_ad)


def get_user_ad(pk):
    user_ad = user_ad_gateway.get_user_ad(pk)
    return UserAdSerializer.serialize_data(user_ad)


def update_user_ad(pk, data):
    if "id" in data:
        data.pop("id")
    user_ad = get_user_ad(pk)
    tags = []
    if data.get("tags"):
        tags = data.get("tags")
    tags.append(user_ad.get("code"))
    if data.get("name"):
        tags.extend(data.get("name").split(" "))
    if data.get("description"):
        tags.extend(data.get("description").split(" "))
    category = category_controller.get_category(data.get("category").get("id"))
    if category.get("name"):
        tags.extend(category.get("name").split(" "))
    tags = list(
        filter(lambda x: True if x and x != " " and x != "," else False, tags)
    )
    tags = [i.replace(",", "") for i in tags]
    data["tags"] = tags
    user_ad = user_ad_gateway.update_user_ad(pk, data)
    return UserAdSerializer.serialize_data(user_ad)


def delete_user_ad(pk):
    user_ad = user_ad_gateway.delete_user_ad(pk)
    return user_ad


def delete_user_ad_admin(pk):
    user_ad = user_ad_gateway.get_user_ad(pk)
    user_ad = UserAdSerializer.serialize_data(user_ad)
    for img in user_ad.get("images"):
        delete_image(pk=img.get("id"))
    user_ad = user_ad_gateway.delete_user_ad(pk, force=True)
    return user_ad
