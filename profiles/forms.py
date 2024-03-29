from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    UserCreationForm, AuthenticationForm
)
from .models import Profile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control mb-2'
        self.fields['email'].widget.attrs['placeholder'] = 'E-Mail'

        self.fields['username'].widget.attrs['class'] = 'form-control mb-2'
        self.fields['username'].widget.attrs['placeholder'] = 'Benutzername'

        self.fields['password1'].widget.attrs['class'] = 'form-control mb-2'
        self.fields['password1'].widget.attrs['placeholder'] = 'Passwort'

        self.fields['password2'].widget.attrs['class'] = 'form-control mb-2'
        self.fields['password2'].widget.attrs['placeholder'] = 'Bestätige Passwort'

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['email', 'password']

    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)


        self.fields['username'].widget.attrs['class'] = 'form-control mb-2'
        self.fields['username'].widget.attrs['placeholder'] = 'Benutzername'

        self.fields['password'].widget.attrs['class'] = 'form-control mb-2'
        self.fields['password'].widget.attrs['placeholder'] = 'Passwort'


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username']

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)


        self.fields['username'].widget.attrs['class'] = 'form-control mb-2'
        self.fields['username'].widget.attrs['placeholder'] = 'Benutzername'

        self.fields['email'].widget.attrs['class'] = 'form-control mb-2'
        self.fields['email'].widget.attrs['placeholder'] = 'E-Mail'

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'image']

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)


        self.fields['bio'].widget.attrs['class'] = 'form-control mb-2'
        self.fields['bio'].widget.attrs['placeholder'] = 'Bio'

        self.fields['image'].widget.attrs['class'] = 'form-control mb-2'
        self.fields['image'].widget.attrs['placeholder'] = 'Bild'