from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from pet.forms import PetForm
from pet.models import Pet
from django.urls import reverse, NoReverseMatch

# Create your views here.
def index(request):
    return render(request, 'pet/index.html')

def pet_view(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = PetForm()

    return render(request, 'pet/pet_form.html', { 'form': form })

def pet_list(request):
    pet = Pet.objects.all().order_by('id')
    context = {'pet': pet}
    return render(request, 'pet/pet_list.html', context)

def pet_edit(request, id_pet):
    pet = Pet.objects.get(id=id_pet)
    if request.method == 'GET':
        form = PetForm(instance=pet)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
        return redirect('pet_list')
    return render(request, 'pet/pet_form.html', { 'form': form })

def pet_delete(request, id_pet):
    pet = Pet.objects.get(id=id_pet)
    if request.method == 'POST':
        pet.delete()
        return redirect('pet_list')
    return render(request, 'pet/pet_delete.html', { 'pet': pet })

class PetList(ListView):
    model = Pet
    template_name = 'pet/pet_list.html'
    
class PetCreate(CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'pet/pet_form.html'

    def get_success_url(self):
        return reverse('pet_list')

class PetUpdate(UpdateView):
    model = Pet
    form_class = PetForm
    template_name = 'pet/pet_form.html'

    def get_absolute_url(self):
        return reverse("pet:pet_form", kwargs={"pk": self.pk})
    
    def get_success_url(self):
        return reverse('pet_list')
    
    
class PetDelete(DeleteView):
    model = Pet
    form_class = PetForm
    template_name = 'pet/pet_delete.html'

    def get_absolute_url(self):
        return reverse("pet:pet_delete", kwargs={"pk": self.pk})
    
    def get_success_url(self):
        return reverse('pet_list')