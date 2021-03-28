from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hackathon.urls')),
]
urlpatterns += staticfiles_urlpatterns()
