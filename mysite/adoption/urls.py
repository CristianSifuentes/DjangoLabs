from django.urls import path
from adoption.views import index

urlpatterns = [
    path('', index),
]
