from django.db import models
from tiposdeatividade.models import tiposDeAtividade
from aluno.models import Aluno
from instrutor.models import Instrutor

# Create your models here.

class Turma(models.Model):
    numero = models.AutoField(primary_key=True,
                              help_text='Numero da turma')
    horarioAula = models.TimeField(help_text='Horario da aula')

    duracaoAula = models.SmallIntegerField(help_text='Duração da aula')

    date_inicial = models.DateField(help_text='Data inicial')

    date_final = models.DateField(help_text='Data Final')

    codigo_atividade = models.ForeignKey(tiposDeAtividade, on_delete=models.CASCADE, null=True, blank=True,
                                         related_name='tiposDeAtividade')
    matricula_monitor = models.ForeignKey(Aluno, null=True, blank=True,
                                         on_delete=models.SET_NULL,
                                         related_name='Aluno')
    id_instrutor = models.ForeignKey(Instrutor, null=True, blank=True,
                                         on_delete=models.CASCADE,
                                         related_name='Instrutor')

    def __str__(self):
        return f'{self.numero} - {self.horarioAula}'
