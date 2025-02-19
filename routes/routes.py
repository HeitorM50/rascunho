from bottle import Bottle, template, redirect, static_file
from models.sistema import SistemaAluguel
from models.carro import Carro

app = Bottle()

# Inicializa sistema com carros
sistema = SistemaAluguel()
modelos = [
    ("Fiat Argo", "ABC1A23", 150),
    ("Volkswagen Gol", "DEF4B56", 140),
    ("Chevrolet Onix", "GHI7C89", 160),
    ("Ford Ka", "JKL0D12", 130),
    ("Hyundai HB20", "MNO3E45", 155),
    ("Renault Kwid", "PQR6F78", 125)
]
for i, (modelo, placa, preco) in enumerate(modelos):
    sistema.adicionar_carro(Carro(i, modelo, placa, preco))

# Rota para arquivos estáticos
@app.route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static')

# Página principal
@app.route('/')
def index():
    carros = sistema.listar_carros()
    return template('views/index.tpl', carros=carros)

# Alugar carro
@app.route('/alugar/<carro_id:int>')
def alugar(carro_id):
    if sistema.alugar_carro(carro_id):
        return redirect('/')
    return "Erro: Carro já alugado."

# Devolver carro
@app.route('/devolver/<carro_id:int>')
def devolver(carro_id):
    if sistema.devolver_carro(carro_id):
        return redirect('/')
    return "Erro: Carro já disponível."