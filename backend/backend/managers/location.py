from django.contrib.auth.models import BaseUserManager
from django.db import models


class LocationQueryset(models.QuerySet):
    def filter_name(self, name):
        return self.filter(name=name)


class LocationManager(BaseUserManager):
    def get_queryset(self):
        return super(LocationManager, self).get_queryset()

