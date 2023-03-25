# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _

from ..utils.core import Core
from ..managers.saved_ad import SavedAdManager, SavedAdQueryset
from ..models.user import User
from ..models.user_ad import UserAd


class SavedAd(Core):
    """
    Description of Saved Ads Model
    """

    user = models.ForeignKey(
        verbose_name=_("User"),
        to=User,
        related_name="saved_ad_user",
        on_delete=models.CASCADE,
    )
    user_ad = models.ForeignKey(
        verbose_name=_("UserAd"),
        to=UserAd,
        related_name="saved_ad",
        on_delete=models.CASCADE,
    )
    objects = SavedAdManager.from_queryset(SavedAdQueryset)()

    class Meta:
        app_label = "backend"
        verbose_name = _("SavedAd")
        verbose_name_plural = _("SavedAds")

    def __str__(self):
        return str(self.id)

    def __unicode__(self):
        return str(self.id)
