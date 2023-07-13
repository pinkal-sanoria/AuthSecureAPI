from django.shortcuts import render
from .serializers import RegisterSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User


# Create your views here.
@api_view(['GET'])
def get_user(request):
    user_data = {
        "username": "pinkal",
        "email": "pinkal@gmail.com",
        "password": "pinkal123"
    }
    serializer = RegisterSerializer(data=user_data)
    if serializer.is_valid():
        username = serializer.validated_data.get('username')
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        user = User. objects. create_user( username=username, email=email , password= password)
        print(user)
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    
