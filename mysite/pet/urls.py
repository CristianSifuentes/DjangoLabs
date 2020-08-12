from django.urls import path
from pet.views import index, pet_view, pet_list

urlpatterns = [
    path('', index, name='index'),
    path('add/', pet_view, name='pet_view'),
    path('list/', pet_list, name='pet_list')

]
