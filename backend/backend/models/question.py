# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _

from ..utils.core import Core
from ..managers.question import QuestionManager, QuestionQueryset
from ..models.category import Category


class Question(Core):
    """
    Description of Question Model
    """

    question = models.TextField(
        _("Question"),
    )

    category = models.ForeignKey(
        verbose_name=_("Category"),
        to=Category,
        related_name="question_category",
        on_delete=models.CASCADE,
    )
    sequence = models.PositiveIntegerField(_("Sequence"), default=0)
    objects = QuestionManager.from_queryset(QuestionQueryset)()

    class Meta:
        app_label = "backend"
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")

    def __str__(self):
        return self.question

    def __unicode__(self):
        return self.question
