from rest_framework import viewsets,  status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Department
from .serializers import DepartmentSerializer


# Create your views here.
class DepartmentViewSet(viewsets.ModelViewSet):
    """
    CRUD API for Department model
    """
    queryset = Department.objects.all().order_by('-created_at')
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """Create a new department"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """Update an existing department"""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """Delete a department"""
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Department deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
