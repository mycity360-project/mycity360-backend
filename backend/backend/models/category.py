# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals
import os
from uuid import uuid4

# lib imports
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

from ..utils.core import Core
from ..managers.category import CategoryManager, CategoryQueryset
from ..constants import SERVER_BASE_URL


phone_regex = RegexValidator(
    regex=r"^\+?1?\d{9,15}$",
    message="Phone number must be entered in the format:"
    " '+999999999'. Up to 15 digits allowed.",
)


def upload_to(instance, filename):
    base, ext = os.path.splitext(filename)
    ext = ext.lower()
    return f"category/{uuid4()}{ext}"


class Category(Core):
    """
    Description of Category Model
    """

    name = models.CharField(
        _("Name"),
        max_length=128,
        unique=True,
    )

    category = models.ForeignKey(
        verbose_name=_("Category"),
        to="self",
        related_name="parent_category",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    icon = models.URLField(_("Image URL"), null=True, blank=True)
    icon_data = models.ImageField(
        _("Image"), null=True, blank=True, upload_to=upload_to
    )

    phone = models.CharField(
        _("Phone Number"),
        max_length=17,
        blank=True,
        null=True,
        validators=[phone_regex],
    )
    sequence = models.PositiveIntegerField(_("Sequence"), default=0)
    is_price = models.BooleanField(
        _("Is Price Required"),
        default=True,
    )
    price_limit = models.FloatField(_("Price Limit"), null=True, blank=True)
    objects = CategoryManager.from_queryset(CategoryQueryset)()

    class Meta:
        app_label = "backend"
        verbose_name = _("Category")
        verbose_name_plural = _("Category")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


@receiver(post_save, sender=Category)
def create_profile(sender, instance, **kwargs):
    if (
        instance.icon_data
        and instance.icon != f"{SERVER_BASE_URL}{instance.icon_data}"
    ):
        instance.icon = f"{SERVER_BASE_URL}{instance.icon_data}"
        instance.save()
