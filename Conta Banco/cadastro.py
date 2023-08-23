class ContaBanco():
    def __init__(self, nome_titular, num_conta, saldo):

        self.__nome_titular = nome_titular
        self.__num_conta = num_conta
        self.__saldo = saldo

                
    def deposito(self,x):
        self.__saldo = self.__saldo + x


    def saque(self,x):
        self.__saldo = self.__saldo - (x + 5)