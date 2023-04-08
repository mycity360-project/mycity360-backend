from django.db import models


class QuestionQueryset(models.QuerySet):
    pass


class QuestionManager(models.Manager):
    def get_queryset(self):
        return super(QuestionManager, self).get_queryset()
