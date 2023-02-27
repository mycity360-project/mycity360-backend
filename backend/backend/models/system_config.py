# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _

from ..utils.core import Core
from ..managers.system_config import SystemConfigManager, SystemConfigQueryset


class SystemConfig(Core):
    """
    Description of State Model
    """

    key = models.CharField(
        _("name"),
        max_length=1024,
        unique=True,
    )
    value = models.CharField(
        _("value"),
        max_length=1024,
    )

    objects = SystemConfigManager.from_queryset(SystemConfigQueryset)()

    class Meta:
        app_label = "backend"
        verbose_name = _("System Config")
        verbose_name_plural = _("System Configs")

    def __str__(self):
        return f"{self.key}--{self.value}"

    def __unicode__(self):
        return f"{self.key}--{self.value}"
