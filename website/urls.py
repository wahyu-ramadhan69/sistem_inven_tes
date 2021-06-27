from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.views import debug
from django.conf.urls.static import static

from django.views.static import serve
from django.conf.urls import url

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('django/', debug.default_urlconf, name='django'),
    path('', include('autentikasi.urls')),
    path('autentikasi/', include('autentikasi.urls')),
    path('pengawas/', include('pengawas.urls')),
    path('petugas/', include('petugas.urls')),
    path('test/', views.test, name='test'),

    url(r'^media/(?P<path>.*)$', serve,
        {'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),

]
