from django.conf.urls import url, include
from django.contrib import admin
from home.views import get_home_index


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_home_index, name="home"),
    url(r'^accounts/', include("accounts.urls")),
    url(r'^blog/', include("blog.urls")),
]
