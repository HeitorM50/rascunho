from bottle import Bottle, request, template, redirect
from models.carro import carro_db


car_app = Bottle()

@car_app.route('/')
def listar_carros():
    usuario = request.get_cookie('usuario', secret='chave_secreta')
    if not usuario:
        return redirect('/auth/login')
    carros = carro_db.listar_carros()
    return template('views/alugar.tpl', usuario=usuario, carros=carros)

@car_app.route('/alugar/<carro_id:int>')
def alugar_carro(carro_id):
    usuario = request.get_cookie('usuario', secret='chave_secreta')
    if not usuario:
        return redirect('/auth/login')
    carro_db.alugar_carro(carro_id)
    return redirect('/carros')
