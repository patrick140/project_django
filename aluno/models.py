from django.db import models
from django.utils import timezone

# Create your models here.

class Aluno(models.Model):
    matricula = models.AutoField(primary_key=True,
                              help_text='Matricula do aluno')
    nome = models.CharField(max_length=70, 
                                 help_text='Nome do aluno')
    dataInicial = models.DateField(null=False,
                                   default=timezone.now(),
                                   help_text='Informe a data inicial de matrícula do aluno')

    dataFinal = models.DateField(null=True,
                                 blank=True,
                                 help_text='Informe a data Final de matrícula do aluno')

    def __str__(self):
        return f'{self.nome} - {self.matricula}'