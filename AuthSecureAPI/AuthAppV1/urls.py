from django.urls import path
from .views import get_user

app_name = 'AuthAppV1'

urlpatterns = [
    path('get-user/', get_user, name='get_user'),
]