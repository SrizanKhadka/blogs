from django.urls import path
from authentication.api.views import UserRegistrationView, LoginAPIView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name="registration"),
    path('login/', LoginAPIView.as_view(), name="Login"),
]

