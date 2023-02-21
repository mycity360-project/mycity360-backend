from rest_framework import serializers
from ..models.user import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
