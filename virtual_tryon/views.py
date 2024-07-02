from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
import os
import logging
from django.conf import settings  # Import settings
from .serializers import FileUploadSerializer

# Configure logging
logging.basicConfig(level=logging.INFO)

@api_view(['POST'])
def handle_file_upload(request):
    if request.method == 'POST':
        user_photo = request.FILES.get('user_photo')
        clothing_photo = request.FILES.get('clothing_photo')
        
        if user_photo and clothing_photo:
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

                return Response({'message': 'Files uploaded successfully.', 'user_photo_path': user_photo_path, 'clothing_photo_path': clothing_photo_path}, status=200)
            except Exception as e:
                logging.error(f"Error saving files: {e}")
                return Response({'error': f'Failed to save files: {e}'}, status=500)
        
        return Response({'error': 'Both files are required.'}, status=400)

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid():
            user_photo = serializer.validated_data.get('user_photo')
            clothing_photo = serializer.validated_data.get('clothing_photo')
            
            if user_photo and clothing_photo:
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
            else:
                return Response({'error': 'Both files are required.'}, status=status.HTTP_400_BAD_REQUEST)
        logging.error("Failed to save file: Invalid data")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
