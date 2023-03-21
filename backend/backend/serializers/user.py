from rest_framework import serializers
from ..models.user import User
from ..serializers.area import AreaSerializers


class UserSerializers(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    phone = serializers.IntegerField(required=True)
    area = AreaSerializers(read_only=True, allow_null=True)
    username = serializers.CharField()

    class Meta:
        model = User
        fields = "__all__"
