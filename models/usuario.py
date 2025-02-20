import json

class UsuarioDB:
    def __init__(self, caminho_arquivo='data/usuarios.json'):
        self.caminho = caminho_arquivo

    def carregar_usuarios(self):
        with open(self.caminho, 'r') as f:
            return json.load(f)

    def autenticar(self, username, password):
        usuarios = self.carregar_usuarios()
        return any(user['username'] == username and user['password'] == password for user in usuarios)

usuario_db = UsuarioDB()