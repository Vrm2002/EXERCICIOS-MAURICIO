class Cadastro():
    def __init__(self, numero_conta, nome, saldo):


        self.__numero_conta = numero_conta
        self.nome = nome
        self.__saldo = saldo


    def deposito(self,x):
        self.__saldo = self.__saldo + x


    def saque(self,x):

        self.__saldo = self.__saldo - (x+5)
        

    def saldo_validate(self):
        if self.__saldo > 0:
            return True
        

        else:
            return False
        

    def get_saldo (self):
        return self.__saldo