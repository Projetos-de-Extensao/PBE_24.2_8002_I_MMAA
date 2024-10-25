from rest_framework import viewsets
from .models import Activity, ActivityType, ActivityMetrics, ActivityHistory
from .serializers import ActivitySerializer, ActivityTypeSerializer, ActivityMetricsSerializer, ActivityHistorySerializer

class ActivityTypeViewSet(viewsets.ModelViewSet):
    queryset = ActivityType.objects.all()
    serializer_class = ActivityTypeSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ActivityMetricsViewSet(viewsets.ModelViewSet):
    queryset = ActivityMetrics.objects.all()
    serializer_class = ActivityMetricsSerializer

class ActivityHistoryViewSet(viewsets.ModelViewSet):
    queryset = ActivityHistory.objects.all()
    serializer_class = ActivityHistorySerializer