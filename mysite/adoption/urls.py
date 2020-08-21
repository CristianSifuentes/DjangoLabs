from django.urls import path
from adoption.views import index
from adoption.views import AdoptionRequestList

urlpatterns = [
    path('', index, name='index'),
    path('listadoptionrequest/', AdoptionRequestList.as_view(), name='requestadoption_list')

    # path('add/', PetCreate.as_view(), name='pet_view'),
    # path('edit/<int:pk>', PetUpdate.as_view(), name='pet_edit'),
    # path('delete/<int:pk>', PetDelete.as_view(), name='pet_delete')


]
