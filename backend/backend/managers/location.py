from django.db import models


class LocationQueryset(models.QuerySet):
    def filter_name(self, name):
        return self.filter(name=name)

    def filter_state(self, state_id):
        return self.filter(state_id=state_id)


class LocationManager(models.Manager):
    def get_queryset(self):
        return super(LocationManager, self).get_queryset()
