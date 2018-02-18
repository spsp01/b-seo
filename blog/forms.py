from django import forms
from django.core import validators
from blog.models import UserProfile
from django.contrib.auth.models import User

class Register(forms.ModelForm):
    #username = forms.CharField(widget=forms.)
    #email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Email'}))
   # password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Hasło'}))
  #  vpassword = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Powtórz Hasło'}))
    class Meta:
        model = User
        fields = ('username', 'email','password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nazwa użytkownika'}),
            'email': forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Hasło'})
        }

  #  hide = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])