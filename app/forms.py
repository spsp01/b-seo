from django import forms
from django.core import validators

class FormName(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}),validators=[validators.MaxLengthValidator(1)])
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class':'textarea'}))
    hide = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

