from django import forms
from adoption.models import Person, AdoptionRequest

class PersonForm(forms.ModelForm):
    
    class Meta:
        model = Person
        
        fields = [
            'name',
            'last_name',
            'age',
            'phone',
            'email',
            'address'
        ]
        labels = {
            'name': 'Name',
            'last_name': 'Last Name',
            'age': 'Age',
            'phone': 'Phone',
            'email': 'Email',
            'address' : 'Address'
        }
        widgets= {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.Select(attrs={'class': 'form-control'}),
            'address' : forms.Select(attrs={'class': 'form-control'})
        }
    
class AdoptionRequestForm(forms.ModelForm):
    
    class Meta:
        model = AdoptionRequest
        
        fields = [
            'pet_number',
            'comment',
        ]
        labels = {
            'pet_number': 'Pet Number',
            'comment': 'Comment',
        }
        widgets= {
            'pet_number': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'})
        }
