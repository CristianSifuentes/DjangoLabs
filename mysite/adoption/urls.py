from django.urls import path
from adoption.views import index
from adoption.views import AdoptionRequestList, AdoptionRequestCreate, AdoptionRequestUpdate, AdoptionRequestDelete

urlpatterns = [
    path('', index, name='index'),
    path('list/', AdoptionRequestList.as_view(), name='adoptionrequest_list'),
    path('add/', AdoptionRequestCreate.as_view(), name='adoptionrequest_add'),
    path('edit/<int:pk>', AdoptionRequestUpdate.as_view(), name='adoptionrequest_edit'),
    path('delete/<int:pk>', AdoptionRequestDelete.as_view(), name='adoptionrequest_delete')


]
