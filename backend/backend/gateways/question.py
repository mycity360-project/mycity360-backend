from django.db.models import Q

from rest_framework.exceptions import ValidationError
from ..models.question import Question
from ..serializers.question import QuestionSerializer
from ..constants import QUESTION_DOES_NOT_EXIST
from ..utils.paginate import paginate_queryset


def list_question(
    is_active=True,
    category_id=None,
    page=1,
    page_size=100,
    ordering=None,
    search=None,
):
    question = Question.objects.all().filter(is_deleted=False)
    if is_active is not None:
        question = question.filter(is_active=is_active)
    if category_id is not None:
        question = question.filter(category_id=category_id)
    if search:
        question = question.filter(
            Q(question__icontains=search)
            | Q(label__icontains=search)
            | Q(placeholder__icontains=search)
        )
    if not ordering:
        ordering = "sequence"
    question = question.order_by(ordering)
    data = paginate_queryset(queryset=question, page=page, page_size=page_size)
    # serializers = QuestionSerializer(data.get("results"), many=True)
    # data["results"] = serializers.data
    return data


def create_question(data):
    question = Question.objects.create(**data)
    # serializers = QuestionSerializer(question)
    # return serializers.data
    return question


def update_question(pk, data):
    try:
        question = Question.objects.filter(is_deleted=False).get(id=pk)
        serializers = QuestionSerializer(question, data)
        if serializers.is_valid(raise_exception=True):
            kwargs = {}
            if data.get("category", {}):
                kwargs["category_id"] = data.get("category").get("id")
            serializers.save(**kwargs)
            # return serializers.data
            return question
    except Question.DoesNotExist:
        raise ValidationError(detail=QUESTION_DOES_NOT_EXIST)


def get_question(pk):
    try:
        question = Question.objects.filter(
            is_deleted=False, is_active=True
        ).get(id=pk)
        # serializers = QuestionSerializer(question)
        # return serializers.data
        return question
    except Question.DoesNotExist:
        raise ValidationError(detail=QUESTION_DOES_NOT_EXIST)


def delete_question(pk):
    try:
        question = Question.objects.filter(is_deleted=False).get(pk=pk)
        return question.delete()
    except Question.DoesNotExist:
        raise ValidationError(detail=QUESTION_DOES_NOT_EXIST)
