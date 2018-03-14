from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^login$', login, name="login"),
    url(r'^logout$', logout, name="logout"),
    url(r'^register$', register, name="register"),
    url(r'^profile$', profile, name="profile")
]
