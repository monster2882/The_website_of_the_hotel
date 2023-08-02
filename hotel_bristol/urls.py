from django.conf.urls.static import static
from django.urls import path

from bristol import settings
from .views import *


urlpatterns = [
    path("", home),
    path("arenda-nomera", rent),
    path("about", about),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)