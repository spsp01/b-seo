from django import forms
from django.core import validators
from blog.models import User

class Register(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Hasło'}))
    vpassword = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Powtórz Hasło'}))
    class Meta:
        model = User
        fields ='__all__'


  #  hide = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])