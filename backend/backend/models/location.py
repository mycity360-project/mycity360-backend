# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _

from .core import Core
from .state import State
from ..managers.location import LocationManager, LocationQueryset


class Location(Core):
    """
    Description of Location Model
    """

    name = models.CharField(
        _("name"),
        max_length=128,
        unique=True,
    )

    state = models.ForeignKey(
        verbose_name=_("State"),
        to=State,
        related_name="location_state",
        on_delete=models.CASCADE,
    )

    objects = LocationManager.from_queryset(LocationQueryset)()

    class Meta:
        app_label = "backend"
        verbose_name = _("location")
        verbose_name_plural = _("locations")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
