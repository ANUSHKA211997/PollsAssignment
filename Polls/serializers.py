from rest_framework import serializers
from .models import Question,Track,Choice

class trackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields='__all__'

class questionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields='__all__'