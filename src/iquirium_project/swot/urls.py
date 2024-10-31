from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'swot', views.FeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
