from django import forms
from django_registration.forms import RegistrationFormUniqueEmail
from django.contrib.auth.models import User



class UserRegistrationForm(RegistrationFormUniqueEmail):
    
    username = forms.CharField(widget=forms.HiddenInput, required=False)

    def clean_username(self):
        return self.cleaned_data['username']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        return password2

    def clean(self):
        if not self.errors:
            self.cleaned_data['username'] = self.cleaned_data['email']
        super(UserRegistrationForm, self).clean()
        return self.cleaned_data