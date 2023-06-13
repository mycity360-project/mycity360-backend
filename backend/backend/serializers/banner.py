from rest_framework import serializers
from ..models.banner import Banner
from ..utils.serializer import serialize_image


class BannerSerializer(serializers.ModelSerializer):
    @classmethod
    def serialize_data(cls, data):
        return dict(
            created_date=data.created_date,
            updated_date=data.updated_date,
            extra_data=data.extra_data,
            is_active=data.is_active,
            id=data.id,
            redirect_url=data.redirect_url,
            area=dict(id=data.area_id),
            image=data.image,
            is_deleted=data.is_deleted,
        )

    class Meta:
        model = Banner
        fields = "__all__"
        depth = 1
