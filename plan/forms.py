from django.forms import ModelForm
from django import forms
from .models import User,Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project    
        fields=[
            'name',
            'headline',
            'description',
            'required',
            'budget',
            'est_length',
            'img'
        ]
        labels={
            'est_length':'Estimated Length',
            'required':'Required Roles',
            'img':'Project Image'
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Project name'}),
            'headline':forms.Textarea(attrs={'class':'form-control','placeholder':'Summarize your project in 2 sentences','cols':2,'rows':2}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Give a detailed description of your project','cols':8,'rows':8}),
            'required':forms.SelectMultiple(attrs={'class':'form-control'}),
            'budget':forms.TextInput(attrs={'class':'form-control','type':'number','placeholder':'Project budget in US $'}),
            'est_length':forms.TextInput(attrs={'class':'form-control','type':'number','placeholder':'Estimate the number of weeks to finish the project'}),
            'img':forms.FileInput(attrs={'class':'form-control-file custom-file'})
        }    