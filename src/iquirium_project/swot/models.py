from django.db import models

# Create your models here.
#
# O modelo criado se basea em:
#
# Usuario - Classe já criada que se relaciona de 1 para muitos com Swot
#   Mas, vai ser necessário criar um campo para armazenar experiência e carreira atual e o nível da carreira atual
#   - Atributos:
#       - experiencia: String
#       - carreiraAtual: String
#       - nivelCarreiraAtual: int
#   - Métodos:
#       - visualizarPerfil(): void
#       - modificarExperiencia(): void
#       - modificarCarreiraAtual(): void
#       - modificarNivelCarreiraAtual(): void
#       - visualizarSwot(): void
#       - listarAnalisesSwot(): void
#
# Swot - Classe que vai armazenar as análises SWOT
#   - Atributos:
#       - usuario: id do usuário que fez a análise
#       - forca: String
#       - fraqueza: String
#       - oportunidade: String
#       - ameaca: String
#       - analiseSwot: String
#       - dataUltimaAnalise: data da última análise
#       - periodoEntreAnalises: int
#       - statusConclusao: boolean
#   - Métodos:
#       - verificarConclusao(): void
#       - criarSwot(): void
#       - preencherSwot(): void
#       - gerarAnaliseSwot(): String
#       - visualizarAnalise(): void
#       - modificarPeriodoEntreAnalises(): void

class Usuario(models.Model):
    experiencia = models.CharField(max_length=100)
    carreiraAtual = models.CharField(max_length=100)
    nivelCarreiraAtual = models.IntegerField()

    def visualizarPerfil(self):
        pass

    def modificarExperiencia(self):
        pass

    def modificarCarreiraAtual(self):
        pass

    def modificarNivelCarreiraAtual(self):
        pass

    def visualizarSwot(self):
        pass

    def listarAnalisesSwot(self):
        pass

    def __str__(self):
        return f'{self.experiencia} - {self.carreiraAtual}'

class Swot(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='swot')
    forca = models.CharField(max_length=100)
    fraqueza = models.CharField(max_length=100)
    oportunidade = models.CharField(max_length=100)
    ameaca = models.CharField(max_length=100)
    analiseSwot = models.CharField(max_length=100)
    dataUltimaAnalise = models.DateTimeField(auto_now_add=True)
    periodoEntreAnalises = models.IntegerField()
    statusConclusao = models.BooleanField()

    def verificarConclusao(self):
        pass

    def criarSwot(self):
        pass

    def preencherSwot(self):
        pass

    def gerarAnaliseSwot(self):
        pass

    def visualizarAnalise(self):
        pass

    def modificarPeriodoEntreAnalises(self):
        pass

    def __str__(self):
        return f'{self.usuario.experiencia} - {self.usuario.carreiraAtual}'
