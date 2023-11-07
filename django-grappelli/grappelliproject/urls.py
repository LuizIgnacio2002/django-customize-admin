from django.urls import path, include
from django.contrib import admin
from grappelli import urls as grappelli_urls

urlpatterns = [
    # ...
    path('admin/', admin.site.urls),
    path('grappelli/', include(grappelli_urls)),
    # ...
]
