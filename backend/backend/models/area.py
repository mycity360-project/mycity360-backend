# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _

from .core import Core
from .location import Location
from ..managers.area import AreaManager, AreaQueryset


class Area(Core):
    """
    Description of Area Model
    """

    name = models.CharField(
        _("name"),
        max_length=128,
        unique=True,
    )
    pincode = models.CharField(
        _("pincode"),
        max_length=128,
        unique=True,
    )
    location = models.ForeignKey(
        verbose_name=_("Location"),
        to=Location,
        related_name="area_location",
        on_delete=models.CASCADE,
    )

    objects = AreaManager.from_queryset(AreaQueryset)()

    class Meta:
        app_label = "backend"
        verbose_name = _("area")
        verbose_name_plural = _("area")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

