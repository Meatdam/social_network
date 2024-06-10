from django.urls import path
from django.contrib.auth.decorators import login_required

from users.apps import UsersConfig
from users.views import UserLoginView, UserRegistrationCreateView, ProfileUpdateView, logout, ConfirmRegister, \
    reset_password

app_name = UsersConfig.name

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserRegistrationCreateView.as_view(), name='registration'),
    path('profile/<int:pk>/', login_required(ProfileUpdateView.as_view()), name='profile'),
    path('logout/', logout, name='logout'),
    path('confirm/', ConfirmRegister.as_view(), name='confirm'),
    path('reset_password/', reset_password, name='reset_password'),
]
