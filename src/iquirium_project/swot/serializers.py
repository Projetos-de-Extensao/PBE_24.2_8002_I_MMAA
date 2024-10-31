from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Swot

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class SwotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Swot
        fields = ['id', 'usuario', 'forca', 'fraqueza', 'oportunidade', 'ameaca', 'analiseSwot', 'dataUltimaAnalise', 'periodoEntreAnalises', 'statusConclusao']