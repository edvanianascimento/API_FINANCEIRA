from dao.sqlite_dao_factory import SqliteDAOFactory
from models.previsao import Previsao
import requests as requests
import config

url_base = 'https://api.hgbrasil.com/weather'.format('?key={0}', config.api_key)


previsaoDAO = None
previsao_hoje = None


def consulta_dados_meteriologicos() -> Previsao:
    res = requests.get(url_base)
    dados = res.json()['results']

    temp_celsius = float(dados['temp'])
    data = str(dados['date'])
    hora = str(dados['time'])
    descricao = str(dados['condition_code'])
    dia_noite = str(dados['description'])
    umidade = int(dados['humidity'])
    velocidade_vento = str(dados['wind_speedy'])
    sunrise = str(dados['sunrise'])
    sunset = str(dados['sunset'])
    condicao = str(dados['condition_slug'])

    return Previsao(temp_celsius=temp_celsius, hora=hora, data=data, descricao=descricao, dia_noite=dia_noite,
                    umidade=umidade, velocidade_vento=velocidade_vento, sunrise=sunrise, sunset=sunset,
                    condicao=condicao)


def carregar_previsao_hoje() -> Previsao:

    registro_previsao_hoje = previsaoDAO.buscar_previsao_hoje()

    if registro_previsao_hoje is None:
        previsao = consulta_dados_meteriologicos()
        salvar_previsao(previsao)
        return previsao
    else:
        registro_previsao_hoje = previsaoDAO.buscar_previsao_hoje()
        return Previsao(registro_previsao_hoje[0], registro_previsao_hoje[1],
                        registro_previsao_hoje[2],
                        registro_previsao_hoje[3],
                        registro_previsao_hoje[4],
                        registro_previsao_hoje[5],
                        registro_previsao_hoje[6],
                        registro_previsao_hoje[7],
                        registro_previsao_hoje[8],
                        registro_previsao_hoje[9],
                        )


def salvar_previsao(previsao) -> None:
    previsaoDAO.adicionar(previsao)


def mostrar_menu():
    print(f'Tempo hoje: ', {previsao_hoje.descricao})
    print(f'Temperatura Celcius: ', {previsao_hoje.temp_celsius})
    print(f'Data: ', {previsao_hoje.data})
    print(f'Hora: ', {previsao_hoje.hora})
    print(f'Umidade: ', {previsao_hoje.umidade})
    print(f'Velocidade do Vento: ', {previsao_hoje.velocidade_vento})
    print(f'Sunrise: ', {previsao_hoje.sunrise})
    print(f'Sunset: ', {previsao_hoje.sunset})
    print(f'Condicao: ', {previsao_hoje.condicao})


if __name__ == '__main__':
    SqliteFactory = SqliteDAOFactory()
    previsaoDAO = SqliteFactory.previsao_dao
    previsao_hoje = carregar_previsao_hoje()
    mostrar_menu()
