from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
import os
import logging
from django.conf import settings
from .serializers import FileUploadSerializer

# Configure logging
logging.basicConfig(level=logging.INFO)

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        user_photo = request.FILES.get('user_photo')
        clothing_photo = request.FILES.get('clothing_photo')
        
        if not user_photo or not clothing_photo:
            return Response({'error': 'Both user_photo and clothing_photo are required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        user_photo_path = os.path.join(settings.MEDIA_ROOT, user_photo.name)
        clothing_photo_path = os.path.join(settings.MEDIA_ROOT, clothing_photo.name)

        try:
            # Save user photo
            with open(user_photo_path, 'wb+') as destination:
                for chunk in user_photo.chunks():
                    destination.write(chunk)
            logging.info(f"User photo saved at: {user_photo_path}")

            # Save clothing photo
            with open(clothing_photo_path, 'wb+') as destination:
                for chunk in clothing_photo.chunks():
                    destination.write(chunk)
            logging.info(f"Clothing photo saved at: {clothing_photo_path}")

            return Response({'message': 'Files uploaded successfully', 'user_photo_path': user_photo_path, 'clothing_photo_path': clothing_photo_path}, status=status.HTTP_200_OK)
        except Exception as e:
            logging.error(f"Error saving files: {e}")
            return Response({'error': f'Failed to save files: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
