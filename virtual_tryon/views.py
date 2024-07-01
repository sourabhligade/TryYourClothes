from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileUploadSerializer
from rest_framework.parsers import MultiPartParser, FormParser  # Add these imports
import os   
from django.conf import settings  # Import settings


@api_view(['POST'])
def handle_file_upload(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        # Handle the uploaded file, e.g., save it to a specific directory or process it
        # Example: save file to media directory
        with open('media/' + uploaded_file.name, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        return Response({'message': 'File uploaded successfully.'}, status=200)
    return Response({'error': 'No file found.'}, status=400)

import logging

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid():
            file = serializer.validated_data['file']
            file_path = os.path.join(settings.MEDIA_ROOT, file.name)
            logging.info(f"Saving file at: {file_path}")
            with open(file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            logging.info(f"File saved at: {file_path}")
            return Response({'message': 'File uploaded successfully', 'file_path': file_path}, status=status.HTTP_200_OK)
        logging.error("Failed to save file")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)