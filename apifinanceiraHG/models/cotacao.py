class Cotacao:

#contr o -- método construtor
#("__" é para encapsulamento, ocultar as inf. e mostrar somente as inf. necessárias)

    def __init__(self,id_cotacao: int = -1, dolar: float = 0.0, euro: float = 0.0, data_hora: str = "") -> None:
        super().__init__()
        self.__id_cotacao = id_cotacao
        self.__dolar = dolar
        self.__euro = euro
        self.__data_hora = data_hora


    @property
    def id(self):
        return self.__id_cotacao


    @property
    def dolar(self):
        return self.__dolar


    @dolar.setter
    def dolar(self, value):
        self.__dolar = value


    @property
    def euro(self):
        return self.__euro


    @euro.setter
    def euro(self, value):
        self.__euro = value


    @property
    def data_hora(self):
        return self.__data_hora

    def __str__(self) -> str:
        return f' {self.__data_hora}, $ {self.__dolar}, € {self.__euro}'
