from django import forms
from django.forms import ModelForm
from .models import Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        
        fields = ('name', 'email', 'contact', 'role', 'salary')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact No.'}),
            'role': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Role'}),
            'salary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Salary'}),
        }
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email' ,'password1','password2']