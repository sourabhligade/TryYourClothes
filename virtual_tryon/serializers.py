# serializers.py
from rest_framework import serializers

class FileUploadSerializer(serializers.Serializer):
    user_photo = serializers.FileField()
    clothing_photo = serializers.FileField()
