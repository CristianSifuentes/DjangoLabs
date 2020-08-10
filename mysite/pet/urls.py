from django.urls import path
from pet.views import index, pet_view

urlpatterns = [
    path('', index, name='index'),
    path('add/', pet_view, name='pet_view')

]
