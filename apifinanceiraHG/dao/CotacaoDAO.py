import sqlite3
from abc import ABC, abstractmethod

import dao.sqlite_dao_factory


class CotacaoDAO(ABC):

    @abstractmethod
    def adicionar(self, adicionar):
        pass

    @abstractmethod
    def selecionar_cotacao(self):
        pass

    @abstractmethod
    def excluir_cotacao(self):
        pass

    @abstractmethod
    def buscar_cotacao_hoje(self):
        pass

