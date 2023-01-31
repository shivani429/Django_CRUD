from dataclasses import fields
from django import forms
from demoapp.models import *
from django.contrib.auth.models import User

        
class DetailsForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = '__all__'    


        

        
