class ContaBanco():
    def __init__(self):

        self.__locker = True
    
    def info(self, nome_titular, num_conta, saldo):

        self.__nome_titular = nome_titular
        self.__num_conta = num_conta
        self.__saldo = saldo


    def deposito(self,x):
        self.__saldo = self.__saldo + x


    def saque(self,x):
        if x < self.__saldo - 5:
            self.__saldo = self.__saldo - (x + 5)
            return True

        else:
            return False


    def cadastro_locker(self, x):
        if x == "False":
            self.__locker = False


class Locker():
    def __init__(self,x):


        if x == True:
            self.__locker = True

        else:
            self.__locker = False

