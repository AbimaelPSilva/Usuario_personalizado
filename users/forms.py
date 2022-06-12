from msilib.schema import Class

from django import forms
from django.contrib.auth import forms

from .models import User


# Externder as froms
class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User
