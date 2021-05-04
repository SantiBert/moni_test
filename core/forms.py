from django import forms
from .models import Lending


class LendingForm(forms.ModelForm):
    class Meta:
        model = Lending
        fields = ['name', 'last_name', 'dni',
                  'gender', 'email', 'amount', 'status', 'error']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'DNI'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Monto'}),
            'gender': forms.Select(attrs={'class': 'form-control'})
        }
        labels = {
            'name': 'Nombre', 'last_name': 'Apellido', 'dni': 'DNI', 'amount': 'Monto a prestar', 'email': 'E-mail', 'gender': 'Género',
        }


class LendingAdminForm(forms.ModelForm):
    class Meta:
        model = Lending
        fields = ['name', 'last_name', 'dni',
                  'gender', 'email', 'amount', 'status', 'error']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'DNI'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Monto'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'error': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Nombre', 'last_name': 'Apellido', 'dni': 'DNI', 'amount': 'Monto a prestar', 'email': 'E-mail', 'gender': 'Género', 'status': 'Aprobado', 'error': 'Error'
        }
