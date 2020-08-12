from django.shortcuts import render, redirect
from django.http import HttpResponse
from pet.forms import PetForm
from pet.models import Pet

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
    pet = Pet.objects.all()
    context = {'pet': pet}
    return render(request, 'pet/pet_list.html', context)