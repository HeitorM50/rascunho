<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Sistema de Aluguel de Carros</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <h1>Sistema de Aluguel de Carros</h1>
    <div class="carros">
        % for carro in carros:
            <div class="carro">
                <h2>{{carro.modelo}}</h2>
                <p>Placa: {{carro.placa}}</p>
                <p>Preço diária: R${{carro.preco_diaria}}</p>
                <p>Status: <strong>{{'Disponível' if carro.disponivel else 'Alugado'}}</strong></p>
                % if carro.disponivel:
                    <a href="/alugar/{{carro.id}}" class="btn">Alugar</a>
                % else:
                    <a href="/devolver/{{carro.id}}" class="btn">Devolver</a>
                % end
            </div>
        % end
    </div>
</body>
</html>