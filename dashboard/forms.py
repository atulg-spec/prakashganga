from django import forms
from .models import *

class ContactUsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Enter your name',
            'phone_number_or_email': 'Phone Number or Email',
            'subject': 'Subject',
            'message': 'Your querry',
        }
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'w-100 form-control p-3 mb-4 border-primary bg-light', 'placeholder': placeholders.get(field_name, '')})
    class Meta:
        model = Contact
        fields = ['name', 'phone_number_or_email', 'subject', 'message']


class OpenDematForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Enter your name',
            'phone_number_or_email': 'Phone Number or Email',
            'age': 'Enter your age',
        }
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'w-100 form-control p-3 mb-4 border-primary bg-light', 'placeholder': placeholders.get(field_name, '')})
    class Meta:
        model = Contact
        fields = ['name', 'phone_number_or_email', 'age']

class InvestmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Enter your name',
            'phone_number_or_email': 'Phone Number or Email',
            'age': 'Enter your age',
            'message': 'Describe youself',
        }
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'w-100 form-control p-3 mb-4 border-primary bg-light', 'placeholder': placeholders.get(field_name, '')})
    class Meta:
        model = Contact
        fields = ['name', 'phone_number_or_email', 'age','message']