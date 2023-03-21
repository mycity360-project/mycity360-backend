from django.contrib.auth.models import BaseUserManager
from django.db import models


class AreaQueryset(models.QuerySet):
    def filter_name(self, name):
        return self.filter(name=name)


class AreaManager(models.Manager):
    def get_queryset(self):
        return super(AreaManager, self).get_queryset()
