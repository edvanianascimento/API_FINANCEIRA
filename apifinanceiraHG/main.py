import locale
import sys
from datetime import datetime
from dao.sqlite_dao_factory import SqliteDAOFactory
from models.cotacao import Cotacao

import requests as requests
import api_key


url_base = 'https://api.hgbrasil.com/finance'.format('?key={0}', api_key.api_key)



locale.setlocale(locale.LC_ALL,'')
data_hora = str(datetime.today().date().strftime('%A, %x'))

cotacaoDAO = None
cotacao_hoje = None


def consultar_dados_financeiros() -> Cotacao:
    res = requests.get(url_base)
    dados = res.json()['results']['currencies']

    dolar = float(dados['USD']['buy'])
    euro = float(dados['EUR']['buy'])
    data_hora = str(datetime.now())

    return Cotacao(dolar = dolar, euro = euro ,data_hora = data_hora)

def carregar_cotacao_hoje() -> Cotacao:
    registro_cotacao_hoje = cotacaoDAO.buscar_cotacao_hoje()

    if registro_cotacao_hoje is None:
        cotacao = consultar_dados_financeiros()
        return cotacao
    else:
        registro_cotacao_hoje = cotacaoDAO.buscar_cotacao_hoje()
        return Cotacao(registro_cotacao_hoje[0], registro_cotacao_hoje[1],
                       registro_cotacao_hoje[2], registro_cotacao_hoje[3])

def salvar_cotacao(cotacao) -> None:
    cotacaoDAO.adicionar(cotacao)

def mostrar_menu():
    print(f'Cotação: {data_hora}')
    print(f'Dólar: $ {cotacao_hoje.dolar}')
    print(f'Euro:  {cotacao_hoje.euro}')
    print(f' Digite o valor de 0 para sair')

    valor_reais = float(input('R$'))
    if valor_reais > 0:
        real_em_dolar = valor_reais * cotacao_hoje.dolar
        real_em_euro = valor_reais * cotacao_hoje.euro
        print(f'\n R$ {valor_reais} = $ {real_em_dolar}')
        print(f'\n R$ {valor_reais} = $ {real_em_euro}')
        print('\n')

    else:
        sys.exit("Encerrando o programa...")


if __name__ == '__main__':
    sqliteFactory = SqliteDAOFactory()
    cotacaoDAO = sqliteFactory.cotacao_dao
    cotacao_hoje = carregar_cotacao_hoje()
    mostrar_menu()







