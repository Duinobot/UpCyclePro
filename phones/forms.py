from django import forms
from .models import Phone, PhoneModel, PhoneStorage, PhoneColor

# Create modelform to add phone
class PhoneCreateForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ('name', 'phonemodel', 'color', 'storage', 'imei', 'price_table', 'listing', 'grade')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phonemodel': forms.Select(attrs={'class': 'form-control'}),
            'color': forms.Select(attrs={'class': 'form-control'}),
            'storage': forms.Select(attrs={'class': 'form-control'}),
            'imei': forms.TextInput(attrs={'class': 'form-control'}),
            'price_table': forms.TextInput(attrs={'class': 'form-control'}),
            'listing': forms.TextInput(attrs={'class': 'form-control'}),
            'grade': forms.TextInput(attrs={'class': 'form-control'}),
        }
