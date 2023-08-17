from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm as DefaultUserCreationForm
from django.contrib.auth.forms import UsernameField


class UserSettingsForm(forms.ModelForm):
    id = forms.CharField(disabled=True, required=False)

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "first_name", "last_name"]


class UserCreationForm(DefaultUserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username",)
        field_classes = {"username": UsernameField}
