from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-feedback/', include('feedback_produto.urls')),
    path('api-swot/', include('swot.urls')),
    path('api-perfil/', include('perfil.urls')),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]