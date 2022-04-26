import sqlite3

from dao.dao_factory import DAOFactory
from dao.sqlite_previsao_dao import SqlitePrevisaoDAO


class SqliteDAOFactory(DAOFactory):

    URL_DB = 'db/dados_tempo.db'

    @staticmethod
    def criar_conexao():
        conexao = None

        try:
            conexao = sqlite3.connect(SqliteDAOFactory.URL_DB)
        except sqlite3.Error as err:
            raise Exception(err)
        return conexao

    def dao_factory(self) -> DAOFactory:
        return SqliteDAOFactory()

    @property
    def previsao_dao(self):
        return SqlitePrevisaoDAO()