from django.urls import path
from .views import RegisterView, LoginView, AuthUserAPIView
    # VerifyEmail

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('user', AuthUserAPIView.as_view(), name='user'),
    # path('verify-email/<uidb64>/<token>', VerifyEmail.as_view(), name='activate'),
]
