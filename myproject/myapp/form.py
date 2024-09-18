from django import forms
from django.forms import inlineformset_factory
from .models import *


class employee_profile_form(forms.ModelForm):
    class Meta:
        model = employee_profile
        fields = [
            'employee_id', 'employee_name','ssb_id', 'nrc_no', 'fathername','mothername',
            'gender',  'dob', 'entrydate', 'department', 'position', 'education', 'phone',
            'address', 'township', 'state_region', 'photo', 'familytable'

        ]
        widgets = {
            'employee_id': forms.TextInput(attrs={'class': 'form-control col-md-6', 'placeholder':'Employee ID'}),
            
            'employee_name': forms.TextInput(attrs={'class': 'form-control col-md-6', 'placeholder':'Employee Name'}),
            'ssb_id': forms.TextInput(attrs={'class': 'form-control col-md-6', 'placeholder':'SSB ID'}),
            'nrc_no': forms.TextInput(attrs={'class': 'form-control col-md-6', 'placeholder':'NRC ID'}),
            'fathername': forms.TextInput(attrs={'class': 'form-control col-md-6', 'placeholder':'Father Name'}),
            'mothername': forms.TextInput(attrs={'class': 'form-control col-md-6', 'placeholder':'Mother Name'}),
            'gender': forms.Select(attrs={'class': 'form-control col-md-2'}),
            
            
                        
            'dob': forms.DateInput(attrs={'class': 'form-control col-md-6', 'type':'date'}),
            
            'entrydate': forms.DateInput(attrs={'class': 'form-control col-md-6', 'type':'date'}),
            'department': forms.Select(attrs={'class': 'form-control col-md-4 custom-select2'}),
            'position': forms.Select(attrs={'class': 'form-control col-md-4 custom-select2'}),
            
            'education': forms.Select(attrs={'class': 'form-control col-md-4 custom-select2'}),
            'phone': forms.TextInput(attrs={'class': 'form-control col-md-6', 'placeholder':''}),
            'address': forms.Textarea(attrs={'class': 'form-control col-md-6', 'placeholder':'နေရပ်လိပ်စာ ဖြည့်ပါ'}),
            'township': forms.Select(attrs={'class': 'form-control col-md-4 custom-select2'}),
            
            'state_region': forms.Select(attrs={'class': 'form-control col-md-4 custom-select2'}),
            
        }

class eduprofileform(forms.ModelForm):
    class Meta:
        model = education_profile
        fields = ['school','education_level', 'from_date', 'to_date']
        widgets = {
            'school': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'School/Uni'}),
            'education_level': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Degree'}),
             'from_date': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
              'to_date': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
        }

class workexpform(forms.ModelForm):
    class Meta:
        model = work_exp
        fields = ['company', 'position', 'from_date', 'to_date']
        widgets = {
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'CompanyName'}),
            'position': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Position'}),
             'from_date': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
              'to_date': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
        }

EduFormSet = inlineformset_factory(
    employee_profile, education_profile, form=eduprofileform,
    extra=1, can_delete=True,
    can_delete_extra=True
)
WorkexpFormSet = inlineformset_factory(
    employee_profile, work_exp, form=workexpform,
    extra=1, can_delete=True,
    can_delete_extra=True
)
