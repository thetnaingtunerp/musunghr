from django import forms
from .models import *


class employee_profile_form(forms.ModelForm):
    class Meta:
        model = employee_profile
        fields = '__all__'
        widgets = {}