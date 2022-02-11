from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [
    path('api/',        include('apiapp.urls')),
    path('catalog/',    include('catalogapp.urls')),
    path('accounts/',   include('customerapp.urls')),
    path('admin/',      admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()