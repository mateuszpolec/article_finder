from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('business', views.business),
    path('entertainment', views.entertainment),
    path('health', views.health),
    path('science', views.science),
    path('sport', views.sport)
]