from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.core.exceptions import ValidationError

"""handling registration of user"""
class CustomUserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'Name', 'Gender', 'Age', 'email', 'Number']

    def clean_phone(self):
        Number = self.cleaned_data.get('Number')

        if not Number.isdigit():
            raise ValidationError("Phone number must contain only digits.")

        if len(Number) != 10:
            raise ValidationError("Phone number must be exactly 10 digits.")

        return Number