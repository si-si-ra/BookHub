from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}




# from rest_framework import serializers
# from .models import User
# from django.contrib.auth import authenticate

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'role', 'password']
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user

# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)

#     def validate(self, data):
#         user = authenticate(username=data['username'], password=data['password'])
#         if not user:
#             raise serializers.ValidationError("Invalid credentials")
#         return user


from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    token = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            raise AuthenticationFailed("Both username and password are required.")
        
        user = authenticate(username=username, password=password)
        if user is None:
            raise AuthenticationFailed("Invalid credentials or user does not exist.")
        
        if not user.is_active:
            raise AuthenticationFailed("User account is inactive.")
        
        return {
            'username': user.username,
            'token': user.auth_token.key if hasattr(user, 'auth_token') else None,
            'role': user.role,
        }