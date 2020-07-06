from django import forms
from django.core import validators
from django.forms import ModelForm
from.models import login

class loginform(forms.ModelForm):
    class Meta:
        model = login
        fields = '__all__'
        widgets={
        'Password': forms.PasswordInput(),
        'ReEnterPassword':forms.PasswordInput(),

        }

    def clean(self):
        super(loginform, self).clean()
        Name = self.cleaned_data.get('Name')
        Password=self.cleaned_data.get("Password")
        ReEnterPassword=self.cleaned_data.get("ReEnterPassword")
        if(len(Name)<5):
            raise forms.ValidationError("Length of Name is too short.Please provide length of Name greater than 5")
        if(ReEnterPassword!=Password):
            raise forms.ValidationError('Please ReEnter the password correctly')

        if not any(i.isupper() for i in Password):
            raise forms.ValidationError("Please enter 1 upper case letter.")

        if not any(i.islower() for i in Password):
            raise forms.ValidationError("Please enter 1 lower case letter.")

        if(len(Password)<6):
            raise forms.ValidationError("Please provide more than 6 characters")

        if not any(i.isnumeric() for i in Password):
            raise forms.ValidationError("Please enter 1 Numeric Value.")

        # for i in range(len(Password)):
        #     ss = ['$', '@', '#', '%']
        #     count=0
        #     if(Password[i] in ss):
        #         count+=1
        # if(count<2):
        #     raise forms.ValidationError("Please enter 2 Special Characters")
