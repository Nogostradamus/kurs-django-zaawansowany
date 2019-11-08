from django.contrib import admin
from django.urls import path
from biblioteka.views import glowna, wyslanie_maila

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', glowna),
    path('email', wyslanie_maila)
]
