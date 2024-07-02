from rest_framework import serializers

class FileUploadSerializer(serializers.Serializer):
    user_photo = serializers.ImageField()
    clothing_photo = serializers.ImageField()
