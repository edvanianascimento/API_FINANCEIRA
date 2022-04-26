from abc import ABC, abstractmethod


class PrevisaoDAO(ABC):

    @abstractmethod
    def adicionar(self, previsao):
        pass

    @abstractmethod
    def selecionar_previsao(self):
        pass

    @abstractmethod
    def excluir_previsao(self, id):
        pass

    @abstractmethod
    def buscar_previsao_hoje(self):
        pass