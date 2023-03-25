from django.db import models


class SavedAdQueryset(models.QuerySet):
    def filter_name(self, name):
        return self.filter(name=name)


class SavedAdManager(models.Manager):
    def get_queryset(self):
        return super(SavedAdManager, self).get_queryset()
