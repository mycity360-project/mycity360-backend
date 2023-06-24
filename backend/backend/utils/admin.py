# -*- coding: utf-8 -*-
"""
Register your models here.
"""
# python imports
from __future__ import unicode_literals

# lib imports
from django.contrib import admin
from django.conf import settings
from django.core.cache import cache


class CustomModelAdmin(admin.ModelAdmin):
    """
    Custom Model Admin
    """

    readonly_fields = ("created_date", "updated_date")
    list_per_page = 10
    list_max_show_all = 1000

    # def has_add_permission(self, request):
    #     # return True if settings.DEBUG else False
    #     return request.user.is_superuser or request.user.groups.filter(name='Manager').exists()
    #
    # def has_change_permission(self, request, obj=None):
    #     # return True if settings.DEBUG else False
    #     return request.user.is_superuser or request.user.groups.filter(name='Manager').exists()
    #
    # def has_delete_permission(self, request, obj=None):
    #     # TODO make it false again later once we found out a way to use shell commands from somewhere
    #     # return True if settings.DEBUG else False
    #     return request.user.is_superuser or request.user.groups.filter(name='Manager').exists()

    def get_actions(self, request):
        actions = super().get_actions(request)
        actions["clear_cache"] = (
            self.clear_cache,
            "clear_cache",
            f"Clear Cache for {self.model._meta.verbose_name_plural}",
        )
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def clear_cache(self, *args, **kwargs):
        """
        Clear cache
        """
        # TODO: Only clear cache for selected models
        # cache.clear()
        # keys = "*"
        cache.delete_many("*")
