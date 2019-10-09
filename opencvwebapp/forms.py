from django import forms
from .models import ImageUploadModel


class UploadImageForm(forms.Form):
    title = forms.CharField(max_length=50)
    image = forms.ImageField()

