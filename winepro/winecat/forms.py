from django import forms
from .models import Wine

class WineForm(forms.ModelForm):
    model=forms.Form
    fields=['country','wine_label','wine_sort']
    class Meta:
        model = Wine
        fields =['country','wine_label','wine_sort']