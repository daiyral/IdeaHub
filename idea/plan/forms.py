from django.forms import ModelForm
from django import forms
from .models import User


class EditUserForm(forms.ModelForm):
    class meta:
        model=User
        fields=[
            'about',
            'jobs',
            'experience'
        ]
        
        widgets={
            'about':forms.Textarea(attrs={'class':'form-control'}),
            'jobs':forms.ChoiceField(attrs={'class':'form-control'}),
            'experience':forms.Textarea(attrs={'class':'form-control'})
        }