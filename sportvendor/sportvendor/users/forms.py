from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserLogin(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegister(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username']

    def save(self, commit=True):
        user = super(UserRegister, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name'],
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


class UserProfile(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(UserProfile, self).__init__(*args, **kwargs)
        self.fields["username"].disabled = True
        self.fields["email"].disabled = True
