from django.contrib import admin
from django.urls import path,include
from .views import hello_world_view
urlpatterns = [
    path('', hello_world_view)
]