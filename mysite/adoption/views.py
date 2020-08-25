from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from adoption.forms import AdoptionRequestForm, PersonForm
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
    template_name = 'adoption/adoptionrequest_form.html'
    form_class = AdoptionRequestForm
    second_form_class = PersonForm

    def get_success_url(self):
        return reverse('adoptionrequest_list')
    
    def get_context_data(self, **kwargs):
        context = super(AdoptionRequestCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            req = form.save(commit=False)
            req.person = form2.save()
            req.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

class AdoptionRequestUpdate(UpdateView):
    model = AdoptionRequest
    second_model = Person
    template_name = 'adoption/adoptionrequest_form.html'
    form_class = AdoptionRequestForm
    second_form_class = PersonForm

    def get_context_data(self, **kwargs):
        context = super(AdoptionRequestUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        req = self.model.objects.get(id=pk)
        person = self.second_model.objects.get(id=req.person_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=person)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_req = kwargs['pk']
        req = self.model.objects.get(id=id_req)
        person = self.second_model.objects.get(id=req.person_id)
        form = self.form_class(request.POST, instance=req)
        form2 = self.second_form_class(request.POST, instance=person)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())
        

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