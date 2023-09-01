from Cadastro_Geral import Pessoa


class Juridico(Pessoa):
    def __init__(self, num_func: int, nome: str, renda_anual: float) -> None:
        super().__init__(nome, renda_anual)

        self.num_func = num_func
        self.__renda_anual = renda_anual

    
    def imposto(self) -> float:

        if self.num_func <= 10:

            imposto = self.__renda_anual * 0.16

            return imposto
        
        else:

            imposto = self.__renda_anual * 0.14

            return imposto

