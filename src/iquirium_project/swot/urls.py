from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from .views import swot_view

router = DefaultRouter()
router.register(r'swot', views.SwotViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('site/', swot_view, name='swot'),
]
