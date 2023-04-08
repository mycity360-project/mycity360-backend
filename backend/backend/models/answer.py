# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _

from ..utils.core import Core
from ..managers.answer import AnswerManager, AnswerQueryset
from ..models.user import User
from ..models.user_ad import UserAd
from ..models.question import Question


class Answer(Core):
    """
    Description of Answer Model
    """

    answer = models.TextField(
        _("Answer"),
    )

    question = models.ForeignKey(
        verbose_name=_("Question"),
        to=Question,
        related_name="answer_question",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        verbose_name=_("User"),
        to=User,
        related_name="answer_user",
        on_delete=models.CASCADE,
    )
    user_ad = models.ForeignKey(
        verbose_name=_("UserAd"),
        to=UserAd,
        related_name="answer_ad",
        on_delete=models.CASCADE,
    )
    objects = AnswerManager.from_queryset(AnswerQueryset)()

    class Meta:
        app_label = "backend"
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")

    def __str__(self):
        return self.answer

    def __unicode__(self):
        return self.answer
