from django.urls import path
from .views import LoginUserView,LogoutUserView,RegisterUserView,TwoFactorAuthenticationView,ActiveTFAView

app_name = 'account'

urlpatterns = [
    path('login/',LoginUserView.as_view(),name='login'),
    path('logout/',LogoutUserView.as_view(),name='logout'),
    path('register/',RegisterUserView.as_view(),name='register'),
    path('login/TFA/',TwoFactorAuthenticationView.as_view(),name = 'TFA'),
    path('TFA/',ActiveTFAView.as_view(),name ='activateTFA' ),
]