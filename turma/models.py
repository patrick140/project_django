from django.db import models

# Create your models here.

class Turma(models.Model):
    numero = models.AutoField(primary_key=True,
                              help_text='Numero da turma')
    horarioAula = models.TimeField(help_text='Horario da aula')

    duracaoAula = models.SmallIntegerField(help_text='Duração da aula')

    dataInicial = models.DateField(help_text='Data inicial')

    dataFinal = models.DateField(help_text='Data Final')

    def __str__(self):
        return f'{self.numero} - {self.horarioAula}'
