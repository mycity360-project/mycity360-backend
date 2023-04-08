from rest_framework import serializers
from ..models.question import Question


class QuestionSerializer(serializers.ModelSerializer):
    @classmethod
    def serialize_data(cls, data):
        if data.get("category"):
            data["category"] = dict(id=data.get("category").get("id"))
        return data

    class Meta:
        model = Question
        fields = "__all__"
        depth = 1
