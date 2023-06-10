# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_mysql.models import ListCharField

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
    field_type = models.CharField(
        _("Field Type"),
        max_length=128,
        blank=True,
        null=True,
        default="Text",
        choices=(
            ("Text", "Text"),
            ("Number", "Number"),
            ("Dropdown", "Dropdown"),
            ("Toggle", "Toggle"),
        ),
    )
    label = models.CharField(
        _("Label"),
        max_length=128,
        blank=True,
        null=True,
    )
    placeholder = models.CharField(
        _("Placeholder"),
        max_length=128,
        blank=True,
        null=True,
    )
    is_required = models.BooleanField(
        _("Is Required"),
        default=False,
    )
    answer_limit = models.PositiveIntegerField(
        _("Answer character limit"),
        default=128,
    )
    values = ListCharField(
        base_field=models.CharField(max_length=128),
        max_length=256,
        null=True,
        blank=True,
    )
    objects = QuestionManager.from_queryset(QuestionQueryset)()

    class Meta:
        app_label = "backend"
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")

    def __str__(self):
        return self.question

    def __unicode__(self):
        return self.question
