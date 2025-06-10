from tiposdeatividade.models import tiposDeAtividade

from titulo.models import Titulo

from aluno.models import Aluno

from instrutor.models import Instrutor

from turma.models import Turma

from django.db import connection

from datetime import date

import random

# gerar valor aleatorio
def gerar_numero_aleatorio_faixa(inicio, fim):
    return random.randint(inicio, fim)

def gerar_numero_aleatorio_sequencia(lista_valores):
    return random.choice(lista_valores)

def gerar_data_aleatoria(tipo_data):
    dia = gerar_numero_aleatorio_faixa(1,28)
    mes = gerar_numero_aleatorio_faixa(1,12)
    ano = 0

    if tipo_data == 'inicial':
        ano = gerar_numero_aleatorio_faixa(1970, 2007)
    elif tipo_data == 'final':
        ano = gerar_numero_aleatorio_faixa(2021, 2024)
    elif tipo_data == 'nascimento':
        ano = gerar_numero_aleatorio_faixa(1970, 2000)

    return date(ano, mes, dia)


#truncar tabelas para zerar o contador de auto-incremento
def truncate_table(nome_tabela):
    with connection.cursor() as cursor:
        cursor.execute(f'DELETE FROM {nome_tabela}')
        cursor.execute(f'DELETE FROM sqlite_sequence WHERE name = "{nome_tabela}"')

def truncar_tabelas():
    truncate_table('turma_turma')
    truncate_table('instrutor_instrutor')
    truncate_table('aluno_aluno')
    truncate_table('titulo_titulo')
    truncate_table('tiposdeatividade_tiposdeatividade')
    

def popular_tiposdeatividade():
    lista_tiposdeatividade = []

    for i in range(1,10):
        lista_tiposdeatividade.append(tiposDeAtividade(descricao='Atividade ' + f'{i:02}')) # i:02 o :02 esta deixando o resultado com duas casas

    tiposDeAtividade.objects.bulk_create(lista_tiposdeatividade)
    

def popular_titulo():
    lista_titulo = []

    for i in range(1,10):
        titulo = Titulo(descricao='Titulo ' + f'{i:02}')
        lista_titulo.append(titulo)

    Titulo.objects.bulk_create(lista_titulo)

def popular_aluno():
    lista_aluno = []
    for i in range(1,50):
        lista_aluno.append(
            Aluno(
                nome = 'Aluno ' + f'{i:02}',
                date_inicial = gerar_data_aleatoria('inicial')
            )
        )
    Aluno.objects.bulk_create(lista_aluno)

def popular_instrutor():
    lista_instrutor = []
    lista_valores_titulo = Titulo.objects.values_list('codigo', flat=True)
    codigo_selecionado = gerar_numero_aleatorio_sequencia(lista_valores_titulo)
    titulo = Titulo.objects.get(pk=codigo_selecionado)

    for i in range(1,15):
        lista_instrutor.append(
            Instrutor(
                nome = 'Instrutor ' + f'{i:02}',
                dataNascimento = gerar_data_aleatoria('nascimento'),
                telefone = f'{gerar_numero_aleatorio_faixa(1, 999999999):09}',
                rg = f'{gerar_numero_aleatorio_faixa(1, 999999999999999):015}',
                ddd = f'{gerar_numero_aleatorio_faixa(1, 60):03}',
                codigo_titulo = titulo    
            )
        )
    Instrutor.objects.bulk_create(lista_instrutor)
    

def popular_turma():
    pass