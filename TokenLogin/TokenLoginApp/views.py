from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, UserRegistrationSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser


class UserRegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            resp='User Register'

            # Create token for the user
            token, created = Token.objects.get_or_create(user=user)

            return Response({'token': token.key,'resp':resp}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class UserLoginAPIView(APIView):
    def post(self, request):
        # Retrieve username and password from request data
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate user
        user = authenticate(username=username, password=password)

        if user:

            # Get details of logged user
            userdetails=CustomUser.objects.get(username=username)
            email=userdetails.email
            phone=userdetails.phone
            gender=userdetails.gender
            age=userdetails.age


            # Create or retrieve token for the user
            token, created = Token.objects.get_or_create(user=user)
            print('Login Successful')
        
            return Response({'token': token.key,'username':username,'email':email,'phone':phone,'gender':gender,'age':age}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

