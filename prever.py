"""
Carrega os valores de receitas conforme o mapeamento.
"""

import pandas as pd
import numpy as np
import logging
import sys
from charset_normalizer import from_path
from io import StringIO
from metodos import metodo

# Configurações
folha0 = (0.02 + 0.09)# crescimento vegetativo + inpc
folha1 = (0.02 + 0.05)# crescimento vegetativo + inpc
folha2 = (0.02 + 0.05)# crescimento vegetativo + inpc
ipca0 = 0.1
ipca1 = 0.08
ipca2 = 0.07

# Configuração do logger
logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.StreamHandler(sys.stdout)
    ],
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)

logging.info('Carregando mapeamentos...')
mapeamento = pd.read_excel(r'mapeamento.xlsx', sheet_name='mapeamento', dtype={
    'codigo': str,
    'descricao': str,
    'metodo': str,
    'ano1': str,
    'ano2': str,
    'ano3': str
})

logging.info('Carregando dados de receita passados...')
dados = StringIO(str(from_path(r'dados/balrec1.csv').best()))
logging.info('\tano base - 1...')
balrec1 = pd.read_csv(dados, sep=';', decimal=',', thousands='.', parse_dates=True, infer_datetime_format=True, dtype={
    'codigo_receita': str,
    'orgao': int,
    'uniorcam': int,
    'receita_orcada': float,
    'receita_realizada': float,
    'recurso_vinculado': int,
    'especificacao_receita': str,
    'tipo_nivel': str,
    'numero_nivel': int,
    'caracteristica_peculiar_receita': int,
    'previsao_atualizada': float,
    'complemento_recurso_vinculado': int,
    'fonte_recurso_stn': int,
    'acompanhamento_execucao_orcamentaria': int,
    'data_inicial': str,
    'data_final': str,
    'data_geracao': str,
    'cnpj': str,
    'entidade': str,
    'arquivo': str
})

logging.info('\tano base - 2...')
dados = StringIO(str(from_path(r'dados/balrec2.csv').best()))
balrec2 = pd.read_csv(dados, sep=';', decimal=',', thousands='.', parse_dates=True, infer_datetime_format=True, dtype={
    'codigo_receita': str,
    'orgao': int,
    'uniorcam': int,
    'receita_orcada': float,
    'receita_realizada': float,
    'recurso_vinculado': int,
    'especificacao_receita': str,
    'tipo_nivel': str,
    'numero_nivel': int,
    'caracteristica_peculiar_receita': int,
    'previsao_atualizada': float,
    'complemento_recurso_vinculado': int,
    'fonte_recurso_stn': int,
    'acompanhamento_execucao_orcamentaria': int,
    'data_inicial': str,
    'data_final': str,
    'data_geracao': str,
    'cnpj': str,
    'entidade': str,
    'arquivo': str
})

logging.info('\tano base - 3...')
dados = StringIO(str(from_path(r'dados/balrec3.csv').best()))
balrec3 = pd.read_csv(dados, sep=';', decimal=',', thousands='.', parse_dates=True, infer_datetime_format=True, dtype={
    'codigo_receita': str,
    'orgao': int,
    'uniorcam': int,
    'receita_orcada': float,
    'receita_realizada': float,
    'recurso_vinculado': int,
    'especificacao_receita': str,
    'tipo_nivel': str,
    'numero_nivel': int,
    'caracteristica_peculiar_receita': int,
    'previsao_atualizada': float,
    'complemento_recurso_vinculado': int,
    # 'fonte_recurso_stn': int,
    # 'acompanhamento_execucao_orcamentaria': int,
    'data_inicial': str,
    'data_final': str,
    'data_geracao': str,
    'cnpj': str,
    'entidade': str,
    'arquivo': str
})


logging.info('\tano base - 4...')
dados = StringIO(str(from_path(r'dados/balrec4.csv').best()))
balrec4 = pd.read_csv(dados, sep=';', decimal=',', thousands='.', parse_dates=True, infer_datetime_format=True, dtype={
    'codigo_receita': str,
    'orgao': int,
    'uniorcam': int,
    'receita_orcada': float,
    'receita_realizada': float,
    'recurso_vinculado': int,
    'especificacao_receita': str,
    'tipo_nivel': str,
    'numero_nivel': int,
    'caracteristica_peculiar_receita': int,
    'previsao_atualizada': float,
    #'complemento_recurso_vinculado': int,
    # 'fonte_recurso_stn': int,
    # 'acompanhamento_execucao_orcamentaria': int,
    'data_inicial': str,
    'data_final': str,
    'data_geracao': str,
    'cnpj': str,
    'entidade': str,
    'arquivo': str
})

logging.info('Preparando receita reestimada no Ano-1')
balrec1['receita_reestimada'] = np.where(balrec1['receita_realizada'] > balrec1['previsao_atualizada'], balrec1['receita_realizada'], balrec1['previsao_atualizada'])

logging.info('Buscando a receita realizada dos anos anteriores...')
valores_1 = []
valores_2 = []
valores_3 = []
valores_4 = []
for index, row in mapeamento.iterrows():
    # codigo = row['codigo']
    # descricao = row['descricao']
    # metodo = row['metodo']
    codigo_1 = row['ano_1']
    codigo_2 = row['ano_2']
    codigo_3 = row['ano_3']
    codigo_4 = row['ano_4']
    val_1 = balrec1[balrec1['codigo_receita']==codigo_1][['codigo_receita', 'receita_reestimada']].groupby(by='codigo_receita').sum()
    if len(val_1) > 0:
        val_1 = round(float(val_1['receita_reestimada'][0]), 2)
    else:
        val_1 = 0.0
    val_2 = balrec2[balrec2['codigo_receita'] == codigo_2][['codigo_receita', 'receita_realizada']].groupby(
        by='codigo_receita').sum()
    if len(val_2) > 0:
        val_2 = round(float(val_2['receita_realizada'][0]), 2)
    else:
        val_2 = 0.0
    val_3 = balrec3[balrec3['codigo_receita'] == codigo_3][['codigo_receita', 'receita_realizada']].groupby(
        by='codigo_receita').sum()
    if len(val_3) > 0:
        val_3 = round(float(val_3['receita_realizada'][0]), 2)
    else:
        val_3 = 0.0
    val_4 = balrec4[balrec4['codigo_receita'] == codigo_4][['codigo_receita', 'receita_realizada']].groupby(
        by='codigo_receita').sum()
    if len(val_4) > 0:
        val_4 = round(float(val_4['receita_realizada'][0]), 2)
    else:
        val_4 = 0.0
    valores_1.append(val_1)
    valores_2.append(val_2)
    valores_3.append(val_3)
    valores_4.append(val_4)
mapeamento['val_1'] = valores_1
mapeamento['val_2'] = valores_2
mapeamento['val_3'] = valores_3
mapeamento['val_4'] = valores_4

logging.info('Calculando as previsões da receita...')
valores0 = []
valores1 = []
valores2 = []
for index, row in mapeamento.iterrows():
    match row['metodo']:
        case 'folha':
            val0, val1, val2 = metodo.indice(folha0, folha1, folha2, row['val_1'])
        case 'media_ipca':
            val0, val1, val2 = metodo.media_indice(ipca0, ipca1, ipca2, row['val_1'], row['val_2'], row['val_3'], row['val_4'])
        case 'ipca':
            val0, val1, val2 = metodo.indice(ipca0, ipca1, ipca2, row['val_1'])
        case 'crescimento':
            val0, val1, val2 = metodo.crescimento(row['val_1'], row['val_2'], row['val_3'], row['val_4'])
        case 'media':
            val0, val1, val2 = metodo.media(row['val_1'], row['val_2'], row['val_3'], row['val_4'])
        case _:
            val0 = 0.0
            val1 = 0.0
            val2 = 0.0
    valores0.append(val0)
    valores1.append(val1)
    valores2.append(val2)
mapeamento['val0'] = valores0
mapeamento['val1'] = valores1
mapeamento['val2'] = valores2

logging.info('Salvando o resultado...')
mapeamento.to_excel(r'output/resultado.xlsx')

logging.info('Processo concluído!')