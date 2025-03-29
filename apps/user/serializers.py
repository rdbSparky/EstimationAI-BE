from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError
from .models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError as DjangoValidationError

class UserSignUpSerializer(serializers.ModelSerializer):
    """
    Serializer for user signup
    """
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ("email", "full_name", "password", "role", "department")
    
    def validate(self, attrs):
        """Password and email validation"""
        email = attrs.get("email").lower()

        try:
            validate_email(email)
        except DjangoValidationError:
            raise ValidationError("Enter a valid email address.")
        
        if User.objects.filter(email=attrs["email"]).exists():
            raise ValidationError("User with this email already exists.")
        
        attrs["email"] = email
        return attrs
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return User.objects.create(**validated_data)
