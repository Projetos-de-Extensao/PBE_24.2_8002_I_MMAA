from rest_framework import viewsets
from .models import Perfil
from .serializers import PerfilSerializer


class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer