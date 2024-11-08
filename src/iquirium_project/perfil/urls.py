from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from .views import perfil_view

router = DefaultRouter()
router.register(r'perfil', views.PerfilViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('site/', perfil_view, name='perfil'),
]
