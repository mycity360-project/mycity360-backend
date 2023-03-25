from django.db import models


class ImageQueryset(models.QuerySet):
    def filter_name(self, name):
        return self.filter(name=name)


class ImageManager(models.Manager):
    def get_queryset(self):
        return super(ImageManager, self).get_queryset()
