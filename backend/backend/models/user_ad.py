# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_mysql.models import ListCharField
from ..utils.core import Core
from ..managers.user_ad import UserAdManager, UserAdQueryset
from ..models.image import Image
from ..models.category import Category
from ..models.user import User
from ..models.area import Area


class UserAd(Core):
    """
    Description of UserAd Model
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
    tags = ListCharField(
        base_field=models.CharField(max_length=10),
        max_length=256,
        null=True,
        blank=True,
    )

    images = models.ManyToManyField(
        verbose_name=_("Images"),
        to=Image,
        null=True,
        blank=True,
    )
    is_featured = models.BooleanField(
        _("Is Featured"),
        default=False,
    )
    price = models.FloatField(_("Price"), default=0)
    category = models.ForeignKey(
        verbose_name=_("Category"),
        to=Category,
        related_name="ad_category",
        on_delete=models.SET_NULL,
        null=True,
    )
    user = models.ForeignKey(
        verbose_name=_("User"),
        to=User,
        related_name="ad_user",
        on_delete=models.CASCADE,
    )
    area = models.ForeignKey(
        verbose_name=_("Area"),
        to=Area,
        related_name="ad_area",
        on_delete=models.SET_NULL,
        null=True,
    )
    objects = UserAdManager.from_queryset(UserAdQueryset)()

    class Meta:
        app_label = "backend"
        verbose_name = _("UserAd")
        verbose_name_plural = _("UserAds")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
