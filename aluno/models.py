from django.db import models

# Create your models here.

class Aluno(models.Model):
    matricula = models.AutoField(primary_key=True,
                              help_text='Matricula do aluno')
    nome = models.CharField(max_length=70, 
                                 help_text='Nome do aluno')
    dataInicial = models.DateField(help_text='Data inicial')

    dataFinal = models.DateField(help_text='Data Final')

    def __str__(self):
        return f'{self.nome} - {self.matricula}'