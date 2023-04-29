from rest_framework import serializers
from ..models.question import Question


class QuestionSerializer(serializers.ModelSerializer):
    values = serializers.ListField(required=False)

    @classmethod
    def serialize_data(cls, data):
        return dict(
            category=dict(id=data.category_id),
            created_date=data.created_date,
            updated_date=data.updated_date,
            extra_data=data.extra_data,
            is_active=data.is_active,
            id=data.id,
            question=data.question,
            sequence=data.sequence,
            field_type=data.field_type,
            label=data.label,
            placeholder=data.placeholder,
            is_required=data.is_required,
            answer_limit=data.answer_limit,
            values=data.values,

        )

    class Meta:
        model = Question
        fields = "__all__"
        depth = 1
