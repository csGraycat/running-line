from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:text>', views.video, name='video'),
]
