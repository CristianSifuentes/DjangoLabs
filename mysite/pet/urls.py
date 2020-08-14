from django.urls import path
from pet.views import index, pet_view, pet_list, pet_edit, pet_delete

urlpatterns = [
    path('', index, name='index'),
    path('add/', pet_view, name='pet_view'),
    path('list/', pet_list, name='pet_list'),
    path('edit/<int:id_pet>', pet_edit, name='pet_edit'),
    path('delete/<int:id_pet>', pet_delete, name='pet_delete')


]
