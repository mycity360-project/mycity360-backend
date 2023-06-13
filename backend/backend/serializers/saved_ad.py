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
            user=dict(id=data.user_id),
            user_ad=dict(id=data.user_ad_id),
            created_date=data.created_date,
            updated_date=data.updated_date,
            extra_data=data.extra_data,
            is_active=data.is_active,
            id=data.id,
            is_deleted=data.is_deleted,
        )

    class Meta:
        model = SavedAd
        fields = "__all__"
        depth = 1
