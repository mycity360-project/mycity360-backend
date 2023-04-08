from django.db import models


class AnswerQueryset(models.QuerySet):
    pass


class AnswerManager(models.Manager):
    def get_queryset(self):
        return super(AnswerManager, self).get_queryset()
