from datetime import datetime

from django.db import models
from django.contrib.auth.models import User  # Reutilizando o modelo de User do Django


class Feedback(models.Model):
    TIPO_FEEDBACK_CHOICES = [
        ('comentarios_gerais', 'Comentários Gerais'),
        ('sugestoes_de_melhoria', 'Sugestões de Melhoria'),
        ('relato_de_erros_ou_problemas_tecnicos', 'Relato de erros ou problemas técnicos'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedback_produto')
    tipo_feedback = models.CharField(max_length=50, choices=TIPO_FEEDBACK_CHOICES)
    data = models.DateTimeField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)

    # # confirmar_recebimento: retorna True se o feedback foi confirmado, False caso contrário para o front
    # def confirmar_recebimento(self):
    #     return f'{self.user.username} registrou com sucesso o feedback {self.tipo_feedback}'

    def __str__(self):
        return f'{self.user.name} - {self.tipo_feedback}'
