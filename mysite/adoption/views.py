from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from adoption.forms import AdoptionRequestForm
from adoption.models import Person, AdoptionRequest
from django.urls import reverse, NoReverseMatch

#Create your views here.
def index(request):
    return HttpResponse("Index adoption")


class AdoptionRequestList(ListView):
    model = AdoptionRequest
    template_name = 'adoption/adoptionrequest_list.html'

class AdoptionRequestCreate(CreateView):
    model = AdoptionRequest
    form_class = AdoptionRequestForm
    template_name = 'adoption/adoptionrequest_form.html'

    def get_success_url(self):
        return reverse('adoptionrequest_list')

class AdoptionRequestUpdate(UpdateView):
     model = AdoptionRequest
     form_class = AdoptionRequestForm
     template_name = 'adoption/adoptionrequest_form.html'

     def get_absolute_url(self):
         return reverse("adoptionrequest:adoptionrequest_form", kwargs={"pk": self.pk})
    
     def get_success_url(self):
         return reverse('adoptionrequest_list')
    
    
class AdoptionRequestDelete(DeleteView):
     model = AdoptionRequest
     form_class = AdoptionRequestForm
     template_name = 'adoption/adoptionrequest_delete.html'

     def get_absolute_url(self):
         return reverse("adoptionrequest:adoptionrequest_form", kwargs={"pk": self.pk})
    
     def get_success_url(self):
         return reverse('adoptionrequest_list')