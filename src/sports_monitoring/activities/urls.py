from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'activity-types', views.ActivityTypeViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'metrics', views.ActivityMetricsViewSet)
router.register(r'history', views.ActivityHistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]