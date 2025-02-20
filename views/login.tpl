<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Login - Aluguel de Carros</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <div class="container">
        <h1>Login</h1>
        % if erro:
            <p class="erro">{{ erro }}</p>
        % end
        <form action="/auth/login" method="post">
            <label>Usuário:</label>
            <input type="text" name="username" required>

            <label>Senha:</label>
            <input type="password" name="password" required>

            <button type="submit">Entrar</button>
        </form>
    </div>
</body>
</html>
