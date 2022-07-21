from django.forms import ModelForm
from django import forms

from .models import Claim


class ClaimForm(ModelForm):
    class Meta:
        model = Claim
        fields = '__all__'
        widgets = {
            'repair_date': forms.DateInput(attrs={'type': 'date'})
        }
