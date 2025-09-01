from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import profile
from django.core.exceptions import ValidationError

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already in use.")
        return email


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg shadow-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500',
                'placeholder': 'Enter your username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg shadow-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500',
                'placeholder': 'Enter your email'
            }),
        }

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image', 'gender', 'age', 'fullname', 'summary']
        widgets = {
            'gender': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg shadow-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500',
                'placeholder': 'Enter your gender'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg shadow-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500',
                'placeholder': 'Enter your age'
            }),
            'fullname': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg shadow-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500',
                'placeholder': 'Enter your full name'
            }),
            'summary': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg shadow-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500',
                'placeholder': 'Write something about yourself'
            }),
        }