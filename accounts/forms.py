from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        # sets the placeholder key/value in the attrs for a widget
        # when the form is instantiated (so the widget already exists)
        self.fields['username'].widget.attrs['placeholder'] = 'Username...'
        self.fields['email'].widget.attrs['placeholder'] = 'Email...'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Firstname...'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Lastname...'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter password...'
        self.fields['password2'].widget.attrs['placeholder'] = 'Re-enter Password...'
    