from django.contrib.auth.models import BaseUserManager
from django.db import models


class SystemConfigQueryset(models.QuerySet):
    def filter_key(self, key):
        return self.filter(key=key)


class SystemConfigManager(models.Manager):
    def get_queryset(self):
        return super(SystemConfigManager, self).get_queryset()
