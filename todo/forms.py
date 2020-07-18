from django import forms
from .models import item


class itemForms(forms.ModelForm):
    class Meta:
        model = item
        fields = ['name', 'done']
