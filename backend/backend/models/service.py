# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals
import os
from uuid import uuid4

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from django.core.validators import RegexValidator
from django.db.models.signals import post_save

from ..utils.core import Core
from ..managers.service import ServiceManager, ServiceQueryset
from ..models.image import Image
from ..constants import SERVER_BASE_URL


phone_regex = RegexValidator(
    regex=r"^\+?1?\d{9,15}$",
    message="Phone number must be entered in the format:"
    " '+999999999'. Up to 15 digits allowed.",
)


def upload_to(instance, filename):
    base, ext = os.path.splitext(filename)
    ext = ext.lower()
    return f"service/{uuid4()}{ext}"


class Service(Core):
    """
    Description of Service Model
    """

    name = models.CharField(
        _("Name"),
        max_length=128,
    )
    description = models.TextField(
        _("Description"),
    )
    code = models.CharField(_("Code"), max_length=128, unique=True)
    phone = models.CharField(
        _("Phone Number"),
        max_length=17,
        blank=True,
        null=True,
        validators=[phone_regex],
    )

    icon = models.URLField(_("Image URL"), null=True, blank=True)
    icon_data = models.ImageField(
        _("Image"), null=True, blank=True, upload_to=upload_to
    )

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


@receiver(post_save, sender=Service)
def create_profile(sender, instance, **kwargs):
    if instance.icon != f"{SERVER_BASE_URL}{instance.icon_data}":
        instance.icon = f"{SERVER_BASE_URL}{instance.icon_data}"
        instance.save()
