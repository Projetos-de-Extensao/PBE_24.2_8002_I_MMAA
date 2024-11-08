from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from .views import feedback_view

router = DefaultRouter()
router.register(r'feedback_produto', views.FeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('site/', feedback_view, name='feedback'),
]
