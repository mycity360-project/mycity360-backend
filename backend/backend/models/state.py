# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _

from ..utils.core import Core
from ..managers.state import StateManager, StateQueryset


class State(Core):
    """
    Description of State Model
    """

    name = models.CharField(
        _("name"),
        max_length=128,
        unique=True,
    )

    objects = StateManager.from_queryset(StateQueryset)()

    class Meta:
        app_label = "backend"
        verbose_name = _("state")
        verbose_name_plural = _("states")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
