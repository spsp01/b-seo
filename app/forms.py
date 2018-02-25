from django import forms
from django.core import validators
from django.forms import ModelForm
from .models import Url

class FormName(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}),validators=[validators.MaxLengthValidator(1)])
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class':'textarea'}))
    hide = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

class SubmitUrlForm(forms.Form):
    urlshort = forms.CharField(label='Submit URL')

    # def clean(self):
    #     cleaned_data = super(SubmitUrlForm,self).clean()
    #     print(cleaned_data)
    #     url = cleaned_data['urlshort']
    #     print(url)

    def clean_urlshort(self):
        urlshort = self.cleaned_data['urlshort']
        url_validator = validators.URLValidator()

        try:
            url_validator(urlshort)
        except:
            print(urlshort)
            raise forms.ValidationError('Błędny adres URL')

        return urlshort


class DateInput(forms.DateInput):
    input_type = 'date'

class AddUrlForm(ModelForm):

    class Meta:
        model = Url
        fields = ['url', 'data_publikacji', 'projekty']
        widgets = {
            'data_publikacji': DateInput(attrs={'class': 'input'}),
            'url': forms.TextInput(attrs={'class': 'input','placeholder': 'Wpisz adres URL'}),
            #'projekty': forms.Select(attrs={'class': 'select'})
        }


    def clean_url(self):
        url = self.cleaned_data['url']
        url_validator = validators.URLValidator()

        try:
            url_validator(url)
        except:
            print(url)
            raise forms.ValidationError('Błędny adres URL')

        return url

