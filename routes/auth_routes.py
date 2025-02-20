from bottle import Bottle, request, response, redirect, template
from models.usuario import usuario_db


auth_app = Bottle()

@auth_app.route('/login', method=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return template('views/login.tpl', erro=None)

    username = request.forms.get('username')
    password = request.forms.get('password')

    if usuario_db.autenticar(username, password):
        response.set_cookie('usuario', username, secret='chave_secreta', path = '/')
        return redirect('/')

    return template('views/login.tpl', erro="Usuário ou senha inválidos.")

@auth_app.route('/logout')
def logout():
    response.delete_cookie('usuario')
    return redirect('/auth/login')