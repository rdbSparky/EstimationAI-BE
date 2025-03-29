from rest_framework import viewsets, status, parsers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import UploadedFile
from .serializers import UploadedFileSerializer
from .cloud_services import S3Object, generate_signed_url


class FileUploadViewSet(viewsets.ModelViewSet):
    """ViewSet for uploading files to S3"""

    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer
    permission_classes = [IsAuthenticated]  # Ensures only authenticated users can upload
    parser_classes = [parsers.MultiPartParser]  # Allows file uploads in multipart form-data

    def create(self, request, *args, **kwargs):
        """Handle file uploads and store media key in the database"""

        file = request.FILES.get("file")  # Get uploaded file
        if not file:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        # Upload to S3
        s3_object = S3Object(file, file.name)
        media_key = s3_object.upload()

        signed_url = generate_signed_url(media_key)

        # Save to the database
        uploaded_file = UploadedFile.objects.create(file_key=media_key, file_name=file.name)

        return Response({"media_key": media_key,"signed_url":signed_url}, status=status.HTTP_201_CREATED)
