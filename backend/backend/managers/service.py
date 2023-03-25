from django.db import models


class ServiceQueryset(models.QuerySet):
    def filter_name(self, name):
        return self.filter(name=name)


class ServiceManager(models.Manager):
    def get_queryset(self):
        return super(ServiceManager, self).get_queryset()
