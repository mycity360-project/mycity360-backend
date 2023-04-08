from ..serializers.question import QuestionSerializer
from ..gateways import question as question_gateway


def list_question(
    is_active=None, category_id=None, page=1, page_size=100, ordering=None
):
    question = question_gateway.list_question(
        is_active=is_active,
        category_id=category_id,
        page=page,
        page_size=page_size,
        ordering=ordering,
    )
    question["results"] = [
        QuestionSerializer.serialize_data(data)
        for data in question.get("results")
    ]
    return question


def create_question(data):
    if "id" in data:
        data.pop("id")
    serializers = QuestionSerializer(data=data)
    if serializers.is_valid(raise_exception=True):
        category = data.pop("category")
        data["category_id"] = category.get("id")
        question = question_gateway.create_question(data)
        return QuestionSerializer.serialize_data(question)


def get_question(pk):
    question = question_gateway.get_question(pk)
    return QuestionSerializer.serialize_data(question)


def update_question(pk, data):
    if "id" in data:
        data.pop("id")
    question = question_gateway.update_question(pk, data)
    return QuestionSerializer.serialize_data(question)


def delete_question(pk):
    question = question_gateway.delete_question(pk)
    return question
