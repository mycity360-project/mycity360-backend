from django.contrib import admin
from django.urls import path, re_path, include
from django.shortcuts import render
from ..views import state, system_config, location


urlpatterns = [
    path("state/", state.state_list),
    path("state/<int:pk>/", state.state_details),
    path("system-config/", system_config.system_config_list),
    path("system-config/<int:pk>/", system_config.system_config_details),
    path("location/", location.location_list),
    path("location/<int:pk>/", location.location_details),
]
