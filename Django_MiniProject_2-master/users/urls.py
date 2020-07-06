from django.urls import path,include
from .views import SignupView
from users import views

urlpatterns=[
    path("signup/" ,SignupView.as_view(),name="signup"),
]