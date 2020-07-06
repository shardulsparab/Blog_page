from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import C_UserCreationForm,C_UserChangeForm
from .models import CustomUser



# Register your models here.

class CustomUserAdmin(UserAdmin):
    model=CustomUser
    add_form=C_UserCreationForm
    form=C_UserChangeForm

admin.site.register(CustomUser,CustomUserAdmin)
# Register your models here.
