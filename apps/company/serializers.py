from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.exceptions import ValidationError as DjangoValidationError
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    """
    Serializer for Company model with validation
    """
    email = serializers.EmailField()

    class Meta:
        model = Company
        fields = ('id', 'owner_name', 'name', 'email')
    
    def validate_email(self, value):
        """Validate email format and uniqueness"""
        try:
            validate_email(value)
        except DjangoValidationError:
            raise ValidationError("Enter a valid email address.")

        if Company.objects.filter(email=value).exists():
            raise ValidationError("Company with this email already exists.")
        return value
    
    def create(self, validated_data):
        """Create a new company with validated data"""
        return Company.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """Update an existing company with validated data"""
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
