from rest_framework import serializers
from .models import Swot


class SwotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Swot
        fields = '__all__'
