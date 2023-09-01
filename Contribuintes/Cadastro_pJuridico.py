from Cadastro_Geral import Pessoa


class Juridico(Pessoa):
    def __init__(self, num_func: int) -> None:
        super().__init__()

        self.num_func = num_func