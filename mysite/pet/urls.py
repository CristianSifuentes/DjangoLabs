from django.urls import path
from pet.views import index, pet_view, pet_list, pet_edit, pet_delete
from pet.views import PetList, PetCreate, PetUpdate, PetDelete

urlpatterns = [
    path('', index, name='index'),
    # path('add/', pet_view, name='pet_view'),
    path('add/', PetCreate.as_view(), name='pet_view'),
    path('list/', PetList.as_view(), name='pet_list'),
    path('edit/<int:pk>', PetUpdate.as_view(), name='pet_edit'),
    path('delete/<int:pk>', PetDelete.as_view(), name='pet_delete')

    # path('edit/<int:id_pet>', pet_edit, name='pet_edit'),
    # path('delete/<int:id_pet>', pet_delete, name='pet_delete')


]
