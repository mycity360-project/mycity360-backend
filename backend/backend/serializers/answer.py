from rest_framework import serializers
from ..models.answer import Answer


class AnswerSerializer(serializers.ModelSerializer):
    @classmethod
    def serialize_data(cls, data):
        return dict(
            user=dict(
                id=data.user_id,
            ),
            user_ad=dict(id=data.user_ad_id),
            question=dict(
                id=data.question_id,
                question=data.question.question,
                label=data.question.label,
            ),
            created_date=data.created_date,
            updated_date=data.updated_date,
            extra_data=data.extra_data,
            is_active=data.is_active,
            id=data.id,
            answer=data.answer,
        )

    class Meta:
        model = Answer
        fields = "__all__"
        depth = 1
