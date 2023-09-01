class Pessoa():
    def __init__(self, nome: str, renda_anual: float) -> None:

        self.nome = nome
        self.__renda_anual = renda_anual

    @property
    def renda(self) -> float:
        return self.__renda_anual
    

    def imposto(self) -> None:
        pass