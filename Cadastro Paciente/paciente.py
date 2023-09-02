from datetime import datetime

class Paciente():
    def __init__(self, nome, telefone, email, genero, data_nascimento, pcd):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.genero = genero
        self.data_nascimento = data_nascimento
        self.pcd = pcd
        self.chegada_fila = datetime.now()
    
    def __str__(self):
        return self.nome