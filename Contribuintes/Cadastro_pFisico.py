from Cadastro_Geral import Pessoa


class Fisica(Pessoa):
    def __init__(self, gastos_saude: float, nome: str, renda_anual: float) -> None:
        super().__init__(nome, renda_anual)

        self.__gastos_saude = gastos_saude
        self.gasto_conf = True if self.__gastos_saude > 0 else False
        self.__renda_anual = renda_anual


    @property
    def gastos_saude(self) -> float:
        return self.__gastos_saude
    

    def imposto(self) -> float:

        if self.__renda_anual < 20000 and self.gasto_conf == False:

            imposto = self.__renda_anual * 0.15

            return imposto
        
        elif self.__renda_anual < 20000 and self.gasto_conf == True:

            imposto = self.__renda_anual * 0.15
            gasto_saude_desc = self.__gastos_saude * 0.5
            imposto = imposto - gasto_saude_desc

            return imposto
        
        elif self.__renda_anual >= 20000 and self.gasto_conf == False:

            imposto = self.__renda_anual * 0.15

            return imposto
        

        elif self.__renda_anual >= 20000 and self.gasto_conf == True:

            imposto = self.__renda_anual * 0.25
            gasto_saude_desc = self.__gastos_saude * 0.5
            imposto = imposto - gasto_saude_desc

            return imposto