from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-feedback/', include('feedback_produto.urls')),
    path('api-swot/', include('swot.urls')),
    path('api-perfil/', include('perfil.urls')),
]