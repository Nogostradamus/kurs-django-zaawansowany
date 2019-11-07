from django.contrib import admin
from django.urls import path
from biblioteka.views import glowna

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', glowna)
]
