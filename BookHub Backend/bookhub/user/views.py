from django.shortcuts import render
from .models import *
from rest_framework import generics
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q




# Create your views here.


class CreateUserView (generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_class=[AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)  # Hash the password
        user.save()

class UserDetailsView (generics.RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    
class UpdateUserView(generics.RetrieveUpdateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class DeleteUserView(generics.DestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer


class UserSearchView(APIView):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('query', None)
        if query:
            # Filter users based on query in username, role, phone_number, or address fields
            users = User.objects.filter(
                Q(username__icontains=query) |
                Q(role__icontains=query) |
                Q(phone_number__icontains=query) |
                Q(address__icontains=query)
            )
        else:
            users = User.objects.all()  # Return all users if no query provided

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    





from rest_framework.authtoken.models import Token
from .models import User
from .serializers import LoginSerializer

class LoginView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        return Response({"detail": "Please send a POST request with username and password to login."}, status=200)

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            user = User.objects.get(username=username)

            token, _ = Token.objects.get_or_create(user=user)
            response_data = serializer.validated_data
            response_data['token'] = token.key

            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)