from django import forms
from django.core import validators

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



