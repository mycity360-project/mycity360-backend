from ..serializers.saved_ad import SavedAdSerializer
from ..gateways import saved_ad as saved_ad_gateway


def list_saved_ad(is_active=None, user_id=None, user_ad_id=None):
    saved_ads = saved_ad_gateway.list_saved_ad(is_active=is_active, user_id=user_id, user_ad_id=user_ad_id)
    saved_ads = [
        SavedAdSerializer.serialize_data(saved_ad) for saved_ad in saved_ads
    ]
    return saved_ads


def create_saved_ad(data):
    if "id" in data:
        data.pop("id")
    serializers = SavedAdSerializer(data=data)
    if serializers.is_valid(raise_exception=True):
        user = data.pop("user")
        if user:
            data["user_id"] = user.get("id")
        user_ad = data.pop("user_ad")
        if user_ad:
            data["user_ad_id"] = user_ad.get("id")
        saved_ad = saved_ad_gateway.create_saved_ad(data)
        return SavedAdSerializer.serialize_data(saved_ad)


def get_saved_ad(pk):
    saved_ad = saved_ad_gateway.get_saved_ad(pk)
    return SavedAdSerializer.serialize_data(saved_ad)


def update_saved_ad(pk, data):
    if "id" in data:
        data.pop("id")
    saved_ad = saved_ad_gateway.update_saved_ad(pk, data)
    return SavedAdSerializer.serialize_data(saved_ad)


def delete_saved_ad(pk):
    saved_ad = saved_ad_gateway.delete_saved_ad(pk)
    return saved_ad
