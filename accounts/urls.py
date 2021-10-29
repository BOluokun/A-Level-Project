from django.urls import path

from django.conf import settings

from . import views

urlpatterns = [
    path('login', views.login, name = 'login'),
    path('create-account', views.create_account, name = 'create_account')
]
