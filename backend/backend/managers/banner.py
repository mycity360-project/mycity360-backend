from django.db import models


class BannerQueryset(models.QuerySet):
    pass


class BannerManager(models.Manager):
    def get_queryset(self):
        return super(BannerManager, self).get_queryset()
