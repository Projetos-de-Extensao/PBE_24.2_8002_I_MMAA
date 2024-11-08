from django.shortcuts import render
from rest_framework import viewsets
from .models import Swot
from .serializers import SwotSerializer

class SwotViewSet(viewsets.ModelViewSet):
    queryset = Swot.objects.all()
    serializer_class = SwotSerializer

def swot_view(request):
    return render(request, 'swot.html')
