from django.db import models


class CategoryQueryset(models.QuerySet):
    def filter_name(self, name):
        return self.filter(name=name)

    def filter_category(self, category_id):
        return self.filter(category_id=category_id)


class CategoryManager(models.Manager):
    def get_queryset(self):
        return super(CategoryManager, self).get_queryset()
