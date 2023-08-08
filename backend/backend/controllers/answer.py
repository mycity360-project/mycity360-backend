from ..serializers.answer import AnswerSerializer
from ..gateways import answer as answer_gateway


def list_answer(
    is_active=True,
    question_id=None,
    user_id=None,
    user_ad_id=None,
    page=1,
    page_size=10,
    ordering=None,
):
    answer = answer_gateway.list_answer(
        is_active=is_active,
        question_id=question_id,
        user_id=user_id,
        user_ad_id=user_ad_id,
        page=page,
        page_size=page_size,
        ordering=ordering,
    )
    answer["results"] = [
        AnswerSerializer.serialize_data(data) for data in answer.get("results")
    ]
    return answer


def create_answer(data):
    if "id" in data:
        data.pop("id")
    serializers = AnswerSerializer(data=data)
    if serializers.is_valid(raise_exception=True):
        question = data.pop("question")
        data["question_id"] = question.get("id")
        user = data.pop("user")
        data["user_id"] = user.get("id")
        user_ad = data.pop("user_ad")
        data["user_ad_id"] = user_ad.get("id")
        answer = answer_gateway.create_answer(data)
        return AnswerSerializer.serialize_data(answer)


def get_answer(pk):
    answer = answer_gateway.get_answer(pk)
    return AnswerSerializer.serialize_data(answer)


def update_answer(pk, data):
    if "id" in data:
        data.pop("id")
    answer = answer_gateway.update_answer(pk, data)
    return AnswerSerializer.serialize_data(answer)


def delete_answer(pk):
    answer = answer_gateway.delete_answer(pk)
    return answer
