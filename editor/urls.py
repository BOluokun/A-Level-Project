from django.urls import path

from django.conf import settings

from . import views

urlpatterns = [
    # e.g. /monica34/editor/3
    path('<str:username>/editor/<int:score_id>/', views.open_editor, name = 'open_editor'),
    path('<str:username>/editor/new', views.make_score, name = 'make_score'),
    # e.g. /monica34/editor/3/i
    path('<str:username>/editor/<int:score_id>/<str:action>', views.edit, name = 'edit'),
    path('home', views.home, name = 'home'),
]
