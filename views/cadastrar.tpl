<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Cadastrar-se</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body class="login-page">
    <div class="login-container">
        <h2>Cadastrar-se</h2>
        % if erro:
            <p class="erro">{{erro}}</p>
        % end
        <form action="/auth/cadastrar" method="post">
            <input type="text" name="usuario" placeholder="Usuário" required>
            <input type="password" name="senha" placeholder="Senha" required>
            <button type="submit">Cadastrar</button>
        </form>
        <a href="/auth/login">Voltar para Login</a>
    </div>
</body>
</html>