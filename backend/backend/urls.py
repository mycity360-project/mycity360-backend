from django.contrib import admin
from django.urls import path, re_path, include
from django.shortcuts import render
from .views import user

def render_react(request):
    return render(request, "index.html")


urlpatterns = [
    path("back-admin", admin.site.urls),
    re_path(r"^$", render_react),
    re_path(r"^(?:.*)/?$", render_react),
    path('students/', user.user_list),
    path('students/', user.user_details),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

]