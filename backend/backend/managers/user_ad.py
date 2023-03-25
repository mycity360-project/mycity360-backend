from django.db import models


class UserAdQueryset(models.QuerySet):
    def filter_name(self, name):
        return self.filter(name=name)


class UserAdManager(models.Manager):
    def get_queryset(self):
        return super(UserAdManager, self).get_queryset()
