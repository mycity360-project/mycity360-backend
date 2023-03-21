from django.contrib import admin
from django.urls import path, re_path, include
from django.shortcuts import render


def render_react(request):
    return render(request, "index.html")


urlpatterns = [
    path("back-admin/", admin.site.urls),
    path("api/v1/", include("backend.routes.v1")),
    path("o/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    re_path(r"^$", render_react),
    re_path(r"^(?:.*)/?$", render_react),
]
