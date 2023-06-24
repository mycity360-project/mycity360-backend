# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver
from ..utils.core import Core
from ..managers.banner import BannerManager, BannerQueryset
from ..models.area import Area
from ..constants import SERVER_BASE_URL


class Banner(Core):
    """
    Description of Banner Model
    """

    redirect_url = models.URLField(
        _("Redirect URL"),
    )

    area = models.ForeignKey(
        verbose_name=_("Area"),
        to=Area,
        related_name="banner_area",
        on_delete=models.CASCADE,
    )
    image = models.URLField(_("Image URL"), null=True, blank=True)
    image_data = models.ImageField(
        _("Image"), null=True, blank=True, upload_to="banner/"
    )

    objects = BannerManager.from_queryset(BannerQueryset)()

    class Meta:
        app_label = "backend"
        verbose_name = _("Banner")
        verbose_name_plural = _("Banners")

    def __str__(self):
        return self.redirect_url

    def __unicode__(self):
        return self.redirect_url


@receiver(pre_save, sender=Banner)
def create_profile(sender, instance, **kwargs):
    instance.image = f"{SERVER_BASE_URL}banner/{instance.image_data.name}"
