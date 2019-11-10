from django.contrib import admin
from django.urls import path
from biblioteka.views import glowna, wyslanie_maila, nowy_form
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('email', wyslanie_maila),
    path('nowy_form', nowy_form),

    path('password_reset', PasswordResetView.as_view()),
    path('password_reset_done',
         PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete',
         PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
