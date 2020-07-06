from django import forms
from django.db import models
from django.core import validators
from django.forms import ModelForm,Textarea
from.models import createblog



class create_blog(forms.ModelForm):
    class Meta:
        model=createblog
        fields='__all__'
        # image = forms.ImageField()
        widgets = {
            'content_blog': Textarea(attrs={'cols': 50, 'rows': 10})

        }
