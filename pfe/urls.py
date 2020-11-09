from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('index/', views.emp),
    path('message/', views.message),
    path('espaceadmin/', views.admin),
]