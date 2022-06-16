from django.contrib import admin
from django.urls import path, re_path
# from django.conf.urls import url, include

urlpatterns = [
    re_path('admin/', admin.site.urls),
    # url(r'^api/', include('countries.urls')),
]
