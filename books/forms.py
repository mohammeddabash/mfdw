from django import forms
from .models import book

class CreateForm(forms.ModelForm):
    class Meta:
        model=book
        fields= '__all__'
        #exclude=(,)

class search(forms.Form):
    search=forms.CharField(label='search')

