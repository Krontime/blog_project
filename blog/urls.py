from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^post_list$', post_list, name="post_list"),
    url(r'^post/(\d+)$', post_details, name="view_post"),
    url(r'^new$', new_post, name="new_post"),
    url(r'^edit/(\d+)$', edit_post, name="edit_post"),
    url(r'^delete/(\d+)$', delete_post, name="delete_post"),
]
