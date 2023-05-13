# Introdução

Desafio de criação de uma API em Python utilizando Flask.

# API

A API criada retorna dados de modelos dos itens do catálogo da empresa Jost, disponível no link: http://catalogo.jost.com.br/

As informações foram inputadas no código através de uma lista de dicionários que contém o nome da peça e os modelos disponíveis. Para que seja possível retornar um JSON com as informações presentes no dicionário, foi utilizada a biblioteca jsonify (no exemplo abaixo, a lista de itens está armazenada na variável "Itens" e o retorno da API está na rota padrão).
```
@app.route('/')
def MostrarTodosItens():
   return(jsonify(Itens))
```

Para rodar o código Python, basta rodar o seguinte comando no terminal: set FLASK_APP=app e posteriormente flask run.

Para acessar o catálogo inteiro no formato JSON, basta acessar a rota padrão (o link aparece como output do *flask run*). Para acessar os modelos de uma peça específica, basta acessar a rota padrão acrescentando /itens/<id_peça>.

O id de cada item do catálogo segue conforme abaixo:

| id | Peça |
| ------------- | ------------- |
| 0 | Quinta-roda |
| 1 | Mesa para Quinta-roda |
| 2 | Pino-rei |
| 3 | Engate de Contêiner |
| 4 | Aparelho de Levantamento |
| 5 | Engate Automático |
| 6 | Ponteira |
| 7 | Engate Esférico |
| 8 | Suspensor Pneumático Semirreboque |
| 9 | Suspensor Pneumático 3º Eixo |
| 10 | Suspensor Pneumático Reposição |
| 11 | Porta Estepe |
| 12 | Hubodômetro |
| 13 | Rala |
| 14 | Suporte Paralama Semirreboque |
| 15 | Kit para Veículo Trator |
| 16 | Enganche Automático - Mercado Externo |
| 17 | Aro Giratorio - Mercado Externo |
| 18 | Enganche de Contenedor - Mercado Externo |
| 19 | Levante Neumático - Mercado Externo |
