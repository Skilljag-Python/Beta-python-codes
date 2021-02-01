from django import forms
from django_registration.forms import RegistrationFormUniqueEmail
from django.contrib.auth.models import User



class UserRegistrationForm(RegistrationFormUniqueEmail):
    
    username = forms.CharField(widget=forms.HiddenInput, required=False)

    def clean_username(self):
        return self.cleaned_data['username']

    def clean(self):
        if not self.errors:
            self.cleaned_data['username'] = self.cleaned_data['email']
        super(UserRegistrationForm, self).clean()
        return self.cleaned_data