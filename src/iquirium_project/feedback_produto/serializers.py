from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Feedback

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'tipo_feedback', 'data', 'hora']
