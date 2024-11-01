from django.db import models

from iquirium_project.perfil.models import Perfil


class Swot(models.Model):
    user = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='swot')
    forca = models.CharField(max_length=100)
    fraqueza = models.CharField(max_length=100)
    oportunidade = models.CharField(max_length=100)
    ameaca = models.CharField(max_length=100)
    analiseSwot = models.CharField(max_length=100)
    dataUltimaAnalise = models.DateTimeField(auto_now_add=True)
    periodoEntreAnalises = models.IntegerField()
    statusConclusao = models.BooleanField()

    def verificar_conclusao(self):
        pass

    def criar_swot(self):
        pass

    def preencher_swot(self):
        pass

    def gerar_analise_swot(self):
        pass

    def visualizar_analise(self):
        pass

    def modificar_periodo_entre_analises(self):
        pass

    def __str__(self):
        return f'{self.user.experiencia} - {self.user.carreiraAtual}'
