from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Resturant
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

class ResturantRegister(forms.ModelForm):
    class Meta:
        model = Resturant
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data.get('Name')
        if Resturant.objects.filter(Name=name).exists():
            raise forms.ValidationError("A restaurant with this name already exists.")
        return name

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if Resturant.objects.filter(phone=phone).exists():
            raise forms.ValidationError("This phone number is already registered.")
        return phone
