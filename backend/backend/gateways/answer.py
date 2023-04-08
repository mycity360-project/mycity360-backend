from rest_framework.exceptions import ValidationError
from ..models.answer import Answer
from ..serializers.answer import AnswerSerializer
from ..constants import ANSWER_DOES_NOT_EXIST
from ..utils.paginate import paginate_queryset


def list_answer(
    is_active=None, question_id=None, user_id=None, user_ad_id=None, page=1, page_size=10, ordering=None
):
    answer = Answer.objects.all().filter(is_deleted=False)
    if is_active is not None:
        answer = answer.filter(is_active=is_active)
    if question_id is not None:
        answer = answer.filter(question_id=question_id)
    if user_id is not None:
        answer = answer.filter(user_id=user_id)
    if user_ad_id is not None:
        answer = answer.filter(user_ad_id=user_ad_id)
    if not ordering:
        ordering = "-pk"
    answer = answer.order_by(ordering)
    data = paginate_queryset(queryset=answer, page=page, page_size=page_size)
    serializers = AnswerSerializer(data.get("results"), many=True)
    data["results"] = serializers.data
    return data


def create_answer(data):
    answer = Answer.objects.create(**data)
    serializers = AnswerSerializer(answer)
    return serializers.data


def update_answer(pk, data):
    try:
        answer = Answer.objects.filter(is_deleted=False).get(id=pk)
        serializers = AnswerSerializer(answer, data)
        if serializers.is_valid(raise_exception=True):
            kwargs = {}
            if data.get("user", {}):
                kwargs["user_id"] = data.get("user").get("id")
            if data.get("user_ad", {}):
                kwargs["user_ad_id"] = data.get("user_ad").get("id")
            if data.get("question", {}):
                kwargs["question_id"] = data.get("question").get("id")
            serializers.save(**kwargs)
            return serializers.data
    except Answer.DoesNotExist:
        raise ValidationError(detail=ANSWER_DOES_NOT_EXIST)


def get_answer(pk):
    try:
        answer = Answer.objects.filter(is_deleted=False).get(id=pk)
        serializers = AnswerSerializer(answer)
        return serializers.data
    except Answer.DoesNotExist:
        raise ValidationError(detail=ANSWER_DOES_NOT_EXIST)


def delete_answer(pk):
    try:
        answer = Answer.objects.filter(is_deleted=False).get(pk=pk)
        return answer.delete()
    except Answer.DoesNotExist:
        raise ValidationError(detail=ANSWER_DOES_NOT_EXIST)
