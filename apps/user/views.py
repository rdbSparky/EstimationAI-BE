from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password
from .models import User
from .serializers import UserSignUpSerializer
from rest_framework.permissions import AllowAny

class UserSignUpAPIView(generics.GenericAPIView):
    """
    API View for User Signup with JWT token response
    """
    serializer_class = UserSignUpSerializer
    permission_classes = [AllowAny,]
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            # Generate JWT token for the newly created user
            token_data = {
                "email": user.email,
                "password": request.data["password"],
            }
            token_serializer = TokenObtainPairSerializer(data=token_data)
            
            if token_serializer.is_valid():
                return Response(
                    {
                        "message": "User successfully created",
                        "access": token_serializer.validated_data["access"],
                        "refresh": token_serializer.validated_data["refresh"],
                    },
                    status=status.HTTP_201_CREATED,
                )
            return Response(token_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
