# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

from django.db import models


class Core(models.Model):
    created_date = models.DateTimeField(verbose_name="Created At", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Updated At", auto_now=True)
    is_deleted = models.BooleanField(verbose_name="Is deleted instance", default=False)
    is_active = models.BooleanField(verbose_name="Is active instance", default=True)
    extra_data = models.JSONField(
        verbose_name="Extra Data", default=dict, blank=True, null=True
    )

    class Meta:
        abstract = True

    # noinspection PyMethodOverriding
    def delete(self, force: bool = False):
        self.is_deleted = True
        if force:
            super().delete()
        self.save()
