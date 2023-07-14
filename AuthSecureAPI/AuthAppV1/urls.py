from django.urls import path
from .views import register_user,login_user

app_name = 'AuthAppV1'

urlpatterns = [
    path('get-user/', register_user, name='get_user'),
    path('login-user/', login_user, name='login_user'),
]