from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    """
    Serializer for Department model
    """
    class Meta:
        model = Department
        fields = ('id', 'name', 'company')
    
    def validate(self, attrs):
        if Department.objects.filter(name=attrs['name'], company=attrs['company']).exists():
            raise ValidationError("A department with this name already exists in this company.")
        return attrs