from django.urls import path

from django.conf import settings

from . import views

urlpatterns = [
    path('<str:username>', views.user_library, name = 'user_library'),
    path('<str:username>/upload/<int:score_id>', views.upload, name = 'upload'),
    path('<str:username>/delete/<int:score_id>', views.delete, name = 'delete'),
    path('<str:username>/public-library', views.public_library, name = 'public_library')
]
