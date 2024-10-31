from rest_framework import viewsets
from .models import Swot
from .serializers import SwotSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Swot.objects.all()
    serializer_class = SwotSerializer
