from Cadastro_Geral import Pessoa


class Fisica(Pessoa):
    def __init__(self, gastos_saude: float) -> None:
        super().__init__()

        self.__gastos_saude = gastos_saude
        self.gasto_conf = True if self.__gastos_saude > 0 else False


    @property
    def gastos_saude(self) -> float:
        return self.__gastos_saude
    

    def imposto(self, valor: float) -> float:
        if self.__gastos_saude < 20000 and self.gasto_conf == False:
            self.

            