from tiposdeatividade.models import tiposDeAtividade

from titulo.models import Titulo

from aluno.models import Aluno

from instrutor.models import Instrutor

from turma.models import Turma

from django.db import connection

#truncar tabelas para zerar o contador de auto-incremento
def truncate_table(nome_tabela):
    with connection.cursor() as cursor:
        cursor.execute(f'DELETE FROM TABLE {nome_tabela}')
        cursor.execute(f'DELETE FROM TABLE sqlite_sequence WHERE name = {nome_tabela}')

def truncar_tabelas():
    truncate_table('turma_turma')
    truncate_table('instrutor_instrutor')
    truncate_table('aluno_aluno')
    truncate_table('titulo_titulo')
    truncate_table('tiposdeatividade_tiposdeatividade')
    pass

def popular_tiposdeatividade():
    pass

def popular_titulo():
    pass

def popular_aluno():
    pass

def popular_instrutor():
    pass

def popular_turma():
    pass