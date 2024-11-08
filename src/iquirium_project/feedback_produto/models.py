from django.db import models
from perfil.models import Perfil


class Feedback(models.Model):
    TIPO_FEEDBACK_CHOICES = [
        ('comments', 'Comentários Gerais'),
        ('sugestion', 'Sugestões de Melhoria'),
        ('relates', 'Relato de erros ou problemas técnicos'),
    ]

    user = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='feedback_produto')
    tipo_feedback = models.CharField(max_length=50, choices=TIPO_FEEDBACK_CHOICES)
    descricao_feedback = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)

    # # confirmar_recebimento: retorna True se o feedback foi confirmado, False caso contrário para o front
    # def confirmar_recebimento(self):
    #     return f'{self.user.username} registrou com sucesso o feedback {self.tipo_feedback}'

    def __str__(self):
        return f'{self.user.nome} - {self.tipo_feedback}'
