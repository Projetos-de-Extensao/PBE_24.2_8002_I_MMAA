from django.db import models


class Perfil(models.Model):
    SEXO_CHOICES = [
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
        ('outro', 'Outro'),
    ]

    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=50, choices=SEXO_CHOICES)
    telefone = models.CharField(max_length=20)
    experiencia = models.CharField(max_length=100)
    carreira_atual = models.CharField(max_length=100)
    nivel_carreira_atual = models.IntegerField()

    def visualizar_perfil(self):
        pass

    def modificar_experiencia(self):
        pass

    def modificar_carreira_atual(self):
        pass

    def modificar_nivel_carreira_atual(self):
        pass

    def visualizar_swot(self):
        pass

    def listar_analises_swot(self):
        pass

    def __str__(self):
        return self.nome
