from .models import FoodImages
from django import forms

class UploadForms(forms.ModelForm):
    class Meta:
        model = FoodImages
        fields = ['name','category','cost','images']