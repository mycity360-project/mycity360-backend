# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from ..utils.core import Core
from ..managers.service import ServiceManager, ServiceQueryset
from ..models.image import Image


phone_regex = RegexValidator(
    regex=r"^\+?1?\d{9,15}$",
    message="Phone number must be entered in the format:"
    " '+999999999'. Up to 15 digits allowed.",
)


class Service(Core):
    """
    Description of Service Model
    """

    name = models.CharField(
        _("Name"),
        max_length=128,
    )
    description = models.CharField(
        _("Description"),
        max_length=128,
    )
    code = models.CharField(_("Code"), max_length=128, unique=True)
    phone = models.CharField(
        _("Phone Number"),
        max_length=17,
        blank=True,
        null=True,
        validators=[phone_regex],
    )

    icon = models.URLField(_("Image"), null=True, blank=True)

    images = models.ManyToManyField(
        verbose_name=_("Images"),
        to=Image,
        null=True,
        blank=True,
    )
    sequence = models.PositiveIntegerField(_("Sequence"), default=0)
    objects = ServiceManager.from_queryset(ServiceQueryset)()

    class Meta:
        app_label = "backend"
        verbose_name = _("Service")
        verbose_name_plural = _("Services")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
