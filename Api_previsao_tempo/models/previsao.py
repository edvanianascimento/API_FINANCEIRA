class Previsao:

    def __init__(self, id: int = -1, temp_celsius: float = 0.0, data: str = '', hora: str = '', descricao: str = '',
                 dia_noite: str = '', umidade: int = 0, velocidade_vento: str = '', sunrise: str = '', sunset: str = '',
                 condicao: str = '') -> None:
        super().__init__()
        self.id = id
        self.temp_celsius = temp_celsius
        self.data = data
        self.hora = hora
        self.descricao = descricao
        self.dia_noite = dia_noite
        self.umidade = umidade
        self.velocidade_vento = velocidade_vento
        self.sunrise = sunrise
        self.sunset = sunset
        self.condicao = condicao

        @property
        def id(self):
            return self.id

        @property
        def temp_celsius(self):
            return self.temp_celsius

        @temp_celsius.setter
        def temp_celsius(self, value):
            self.temp_celsius = value

        @property
        def data(self):
            return self.data

        @data.setter
        def data(self, value):
            self.data = value

        @property
        def hora(self):
            return self.hora

        @hora.setter
        def hora(self, value):
            self.hora = value

        @property
        def descricao(self):
            return self.descricao

        @descricao.setter
        def descricao(self, value):
            self.descricao = value

        @property
        def dia_noite(self):
            return self.dia_noite

        @dia_noite.setter
        def dia_noite(self, value):
            self.dia_noite = value

        @property
        def umidade(self):
            return self.umidade

        @umidade.setter
        def umidade(self, value):
            self.umidade = value

        @property
        def velocidade_vento(self):
            return self.velocidade_vento

        @velocidade_vento.setter
        def velocidade_vento(self, value):
            self.velocidade_vento = value

        @property
        def sunrise(self):
            return self.sunrise

        @sunrise.setter
        def sunrise(self, value):
            self.sunrise = value

        @property
        def sunset(self):
            return self.sunset

        @sunset.setter
        def sunset(self, value):
            self.sunset = value

        @property
        def condicao(self):
            return self.condicao

        @condicao.setter
        def condicao(self, value):
            self.condicao = value

        def __str__(self) -> str:
            return f'{self.temp_celsius}'




