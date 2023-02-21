from django.contrib.auth.models import BaseUserManager
from django.db import models


class StateQueryset(models.QuerySet):
    def filter_name(self, name):
        return self.filter(name=name)


class StateManager(BaseUserManager):
    def get_queryset(self):
        return super(StateManager, self).get_queryset()

