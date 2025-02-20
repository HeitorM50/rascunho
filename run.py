from bottle import Bottle, run, redirect, request,static_file
from routes.auth_routes import auth_app
from routes.car_routes import car_app

app = Bottle()

app.mount('/auth', auth_app)
app.mount('/carros', car_app)

@app.route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static')

@app.route('/')
def home():
    usuario = request.get_cookie('usuario', secret='chave_secreta')
    if not usuario:
        return redirect('/auth/login')
    return redirect('/carros')

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True, reloader=True)