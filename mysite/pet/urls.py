from django.urls import path
from pet.views import index

urlpatterns = [
    path('', index),
]
