from django import forms
from core import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    email = forms.CharField(max_length=65,label="Registered Email",help_text="Enter your Registered Email-id")
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email", required=True, help_text="Enter Email")
    email_confirmation = forms.EmailField(label="Email confirmation", required=True, help_text="Confirm Email")

    class Meta:
        model = User
        fields = ['email', 'email_confirmation','password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        email_confirmation = cleaned_data.get("email_confirmation")
        if email_confirmation and email and email_confirmation != email:
            raise forms.ValidationError("The two email fields didn't match.")
        return cleaned_data
    
# class LoginForm(forms.Form):
#     email = forms.CharField(max_length=65, label="Registered Email", help_text="Enter your Registered Email-id")
#     password = forms.CharField(max_length=65, widget=forms.PasswordInput)

#     def clean(self):
#         cleaned_data = super().clean()
#         email = cleaned_data.get('email')
#         password = cleaned_data.get('password')

#         if email and password:
#             user = authenticate(username=email, password=password)

#             if user is None:
#                 raise forms.ValidationError("Invalid login credentials. Please try again.")

#         return cleaned_data
