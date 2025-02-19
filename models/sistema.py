from .carro import Carro

class SistemaAluguel:
    def __init__(self):
        self.carros = []

    def adicionar_carro(self, carro):
        self.carros.append(carro)

    def listar_carros(self):
        return self.carros

    def alugar_carro(self, carro_id):
        carro = self.carros[carro_id]
        if carro.disponivel:
            carro.disponivel = False
            return True
        return False

    def devolver_carro(self, carro_id):
        carro = self.carros[carro_id]
        if not carro.disponivel:
            carro.disponivel = True
            return True
        return False