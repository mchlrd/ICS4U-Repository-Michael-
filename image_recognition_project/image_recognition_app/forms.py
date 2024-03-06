from django import forms
from .models import UploadedImage

class ImageUploadedForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['image']
