from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from auth_api.views import UserRegistrationView

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="user_registration"),
    path("token/", obtain_auth_token),
]
