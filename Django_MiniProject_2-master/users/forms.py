from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser

class C_UserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=("username","email")


class C_UserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields =UserChangeForm.Meta.fields