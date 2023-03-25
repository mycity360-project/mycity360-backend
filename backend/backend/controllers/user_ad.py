from ..serializers.user_ad import UserAdSerializer
from ..gateways import user_ad as user_ad_gateway


def list_user_ad(is_active):
    user_ads = user_ad_gateway.list_user_ad(is_active=is_active)
    user_ads = [
        UserAdSerializer.serialize_data(user_ad) for user_ad in user_ads
    ]
    return user_ads


def create_user_ad(data):
    if "id" in data:
        data.pop("id")
    serializers = UserAdSerializer(data=data)
    if serializers.is_valid(raise_exception=True):
        category = data.pop("category")
        if category:
            data["category_id"] = category.get("id")
        user = data.pop("user")
        if user:
            data["user_id"] = user.get("id")
        area = data.pop("area")
        if area:
            data["area_id"] = area.get("id")
        user_ad = user_ad_gateway.create_user_ad(data)
        return UserAdSerializer.serialize_data(user_ad)


def get_user_ad(pk):
    user_ad = user_ad_gateway.get_user_ad(pk)
    return UserAdSerializer.serialize_data(user_ad)


def update_user_ad(pk, data):
    if "id" in data:
        data.pop("id")
    user_ad = user_ad_gateway.update_user_ad(pk, data)
    return UserAdSerializer.serialize_data(user_ad)


def delete_user_ad(pk):
    user_ad = user_ad_gateway.delete_user_ad(pk)
    return user_ad
