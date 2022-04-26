import sqlite3
import dao.sqlite_dao_factory as dao
from dao.PrevisaoDAO import PrevisaoDAO

class SqlitePrevisaoDAO(PrevisaoDAO):
    def adicionar(self, previsao):

        conexao = dao.SqliteDAOFactory.criar_conexao()
        cursor = conexao.cursor()

        query = 'INSERT INTO PREVISAO VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        registro = (previsao.temp_celsius, previsao.hora, previsao.data, previsao.descricao, previsao.dia_noite,
                    previsao.umidade, previsao.velocidade_vento, previsao.sunrise, previsao.sunset, previsao.condicao)

        try:
            cursor.execute(query, registro)
            conexao.commit()
        except sqlite3.Error as err:
            raise Exception(f'Erro: {err}')
        finally:
            if conexao:
                conexao.close()

    def selecionar_previsao(self):
        pass

    def excluir_previsao(self, id):
        pass

    def pesquisar_previsao(self):
        pass

    def buscar_previsao_hoje(self):
        conexao = dao.SqliteDAOFactory.criar_conexao()
        cursor = conexao.cursor()
        query = 'SELECT * FROM PREVISAO WHERE TIME(HORA) = TIME();'

        try:
            dados = cursor.execute(query).fetchone()
        except sqlite3.Error as e:
            raise Exception(f'Erro: {e}')
        finally:
            if conexao:
                conexao.close





