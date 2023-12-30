

from django import forms
from .models import Earnings, Expenses, Service
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
class LoginForm(AuthenticationForm):
    pass
class EarningsForm(forms.ModelForm):
    class Meta:
        model = Earnings
        fields = ['amount', 'source' ,'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ['amount', 'description', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User  # Assuming you have imported User from django.contrib.auth.models
        fields = ['username', 'password']


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['client_name', 'client_phone', 'client_email', 'service_description', 'months_valid','amount_due']

    due_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))  # Use a date input for due_date


    def clean_amount_due(self):
        amount_due = self.cleaned_data.get('amount_due')
        if amount_due < 0:
            raise forms.ValidationError('Amount due must be a positive number.')
        return amount_due