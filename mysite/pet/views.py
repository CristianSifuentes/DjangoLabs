from django.shortcuts import render, redirect
from django.http import HttpResponse
from pet.forms import PetForm

# Create your views here.
def index(request):
    return render(request, 'pet/index.html')

def pet_view(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
        return redirect('pet:index')
    else:
        form = PetForm()

    return render(request, 'pet/pet_form.html', { 'form': form })