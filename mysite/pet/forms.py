from django import forms
from pet.models import Pet

class PetForm(forms.ModelForm):
    
    class Meta:
        model = Pet
        
        fields = [
            'name',
            'gender',
            'age',
            'redemption_date',
            'person',
            'vaccine'
        ]
        labels = {
            'name': 'Name',
            'gender': 'Gender',
            'age': 'Age',
            'redemption_date': 'Redemption Date',
            'person': 'Person',
            'vaccine' : 'Vaccine'
        }
        widgets= {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'redemption_date': forms.TextInput(attrs={'class': 'form-control'}),
            'person': forms.Select(attrs={'class': 'form-control'}),
            'vaccine' : forms.CheckboxSelectMultiple()
        }
