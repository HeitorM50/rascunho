<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Aluguel de Carros</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <div class="container">
        <h1>Bem-vindo, {{ usuario }}!</h1>
        <h2>Carros Disponíveis:</h2>
        <ul>
            % for carro in carros:
                <li>
                    <span><strong>{{ carro['modelo'] }}</strong> - {{ 'Disponível' if carro['disponivel'] else 'Indisponível' }}</span>
                    % if carro['disponivel']:
                        <a href="/carros/alugar/{{ carro['id'] }}" class="btn-alugar">Alugar</a>
                    % else:
                        <span>Indisponível</span>
                    % end
                </li>
            % end
        </ul>
        <a href="/auth/logout" class="btn-sair">Sair</a>
    </div>
</body>
</html>
