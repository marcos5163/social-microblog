import email
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length = 100)
    password = serializers.CharField(max_length = 100, min_length = 5)
