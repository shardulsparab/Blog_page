from django.shortcuts import render
from django.views.generic import CreateView
from .forms import C_UserCreationForm
from django.urls import reverse_lazy

# Create your views here.
class SignupView(CreateView):
    form_class =C_UserCreationForm
    success_url= reverse_lazy("login")
    template_name="signup.html"


# Create your views here.
