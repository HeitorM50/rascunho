import json

class CarroDB:
    def __init__(self, caminho_arquivo='data/carros.json'):
        self.caminho = caminho_arquivo

    def carregar_carros(self):
        with open(self.caminho, 'r') as f:
            return json.load(f)

    def salvar_carros(self, carros):
        with open(self.caminho, 'w') as f:
            json.dump(carros, f, indent=4)

    def listar_carros(self):
        return self.carregar_carros()

    def alugar_carro(self, carro_id):
        carros = self.carregar_carros()
        for carro in carros:
            if carro['id'] == carro_id and carro['disponivel']:
                carro['disponivel'] = False
                self.salvar_carros(carros)
                break

carro_db = CarroDB()