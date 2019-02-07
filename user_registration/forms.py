from django import forms
from django.core import validators
from django.contrib.auth.models import User
from user_registration.models import GreenUser

class formName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']

        if vemail != email:
            raise forms.ValidationError("Emails should match")


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        help_texts = {
            'username': None,
        }
        fields = ['username', 'email', 'password']

class GreenUserForm(forms.ModelForm):
    class Meta:
        model = GreenUser
        exclude = ["creation_date", "user"]
