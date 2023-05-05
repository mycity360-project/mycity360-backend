# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from ..utils.core import Core
from ..managers.category import CategoryManager, CategoryQueryset
from ..utils.services import get_file_path
from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()

phone_regex = RegexValidator(
    regex=r"^\+?1?\d{9,15}$",
    message="Phone number must be entered in the format:"
    " '+999999999'. Up to 15 digits allowed.",
)


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

    icon = models.ImageField(
        verbose_name=_("Icon"),
        max_length=1024,
        null=True,
        blank=True,
        upload_to=get_file_path,
        storage=gd_storage,
    )
    url = models.URLField(
        _("Image"),
        null=True,
        blank=True
    )
    phone = models.CharField(
        _("Phone Number"),
        max_length=17,
        blank=True,
        null=True,
        validators=[phone_regex],
    )
    sequence = models.PositiveIntegerField(_("Sequence"), default=0)
    objects = CategoryManager.from_queryset(CategoryQueryset)()

    class Meta:
        app_label = "backend"
        verbose_name = _("Category")
        verbose_name_plural = _("Category")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
