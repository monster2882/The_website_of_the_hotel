from django.contrib import admin
from django.urls import path, include

from hotel_bristol.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('hotel_bristol.urls'))
]

handler404 = pageNotFound
