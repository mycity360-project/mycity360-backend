from rest_framework import serializers
from ..models.answer import Answer


class AnswerSerializer(serializers.ModelSerializer):
    @classmethod
    def serialize_data(cls, data):
        return dict(
            user=dict(id=data.get("user").get("id")),
            user_ad=dict(id=data.get("user_ad").get("id")),
            question=dict(id=data.get("question").get("id"), question=data.get("question").get("question")),
            created_date=data.get("created_date"),
            updated_date=data.get("updated_date"),
            extra_data=data.get("extra_data"),
            is_active=data.get("is_active"),
            id=data.get("id"),
            answer=data.get("answer"),
        )

    class Meta:
        model = Answer
        fields = "__all__"
        depth = 1
