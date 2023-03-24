from rest_framework import serializers
from ..models.saved_ad import SavedAd
from ..serializers.user import UserSerializer
from ..serializers.user_ad import UserAdSerializer


class SavedAdSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_ad = UserAdSerializer(read_only=True)

    @classmethod
    def serialize_data(cls, data):
        return dict(
            user=dict(id=data.get("user").get("id")),
            user_ad=dict(id=data.get("user_ad").get("id")),
            created_date=data.get("created_date"),
            updated_date=data.get("updated_date"),
            extra_data=data.get("extra_data"),
            is_active=data.get("is_active"),
            id=data.get("id"),
        )

    class Meta:
        model = SavedAd
        fields = "__all__"
        depth = 1
