from django.shortcuts import render
from .serializers import RegisterSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

@api_view(['POST','GET'])
def register_user(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            user = User.objects.create_user(username=username, email=email, password=password, is_staff=True)
            print(user)
            return Response(serializer.data, status=201)  
        else:
            return Response(serializer.errors, status=400)  
    elif request.method == 'GET':
        users = User.objects.all()  
        serializer = RegisterSerializer(users, many=True)
        return Response(serializer.data, status=200)
    else:
        return Response({'message': 'Invalid request method'}, status=405) 
    
@api_view(['POST'])
def login_user(request):
    if request.method=='POST':
        email = request.data.get('email')
        password = request.data.get('password')
        if email and password:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return Response({'message': 'Login successful'}, status=200)
            else:
                return Response({'message': 'Invalid credentials'}, status=400)
    else:
        return Response({'message': 'Invalid request method'}, status=405) 

        