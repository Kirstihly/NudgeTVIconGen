'''
    If you meet any problems,
    please contact
    Leying Hu
    hu.leying@columbia.edu
'''
from django import forms
from .models import *

class ImageForm(forms.ModelForm):
    
    class Meta:
        model = Shortener
        fields = ['urls_shortened', 'icon_image']
