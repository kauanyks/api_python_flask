from flask import Flask, jsonify

# Foi criada uma instância do Flask e salva na variável app. 
# É essa variável que representa a aplicação Flask que está sendo criada
app = Flask(__name__)

Itens = [
    {
        'nome': 'Quinta-roda',
        'modelos': ['CALIBRADOR LIMITE DE DESGASTE 2"', 'JSK 37C - 2"', 'JSK 37C - 2" [CHASSI DESLIZANTE]', 'JSK 37CW - 2" [CHASSI DESLIZANTE]', 'JSK 37CW - 2" [COM PLACAS POLIMÉRICAS]', 'JSK 37CX - 2"', 'JSK 37CXW - 2"', 'JSK 38C - 2" [REFORÇADA]', 'JSK 38C - 3.1/2" [REFORÇADA]', 'JSK 38G - 2" [OSCILANTE]', 'JSK 38G - 3.1/2" [OSCILANTE]', 'JSK 39CS - 3.1/2" [COM PLACAS DE DESGASTE]', 'SENSORES DE ACOPLAMENTO E LUBETRONIC']
    },
    {
        'nome': 'Mesa para Quinta-roda',
        'modelos': ['MESAS ONDULADAS', 'MESAS ONDULADAS DOG BONE SHAPE', 'MESAS PLANAS', 'MESAS PLANAS REFORÇADAS', 'MESAS PLANAS [16MM]']
    },
    {
        'nome': 'Pino-rei',
        'modelos': ['PINO-REI 2" - PARA CHAPA DE 10MM', 'PINO-REI 2" - PARA CHAPA DE 12MM', 'PINO-REI 2" - PARA CHAPA DE 8MM', 'PINO-REI 3.1/2" - 12 FUROS [FURO CENTRAL]', 'PINO-REI 3.1/2" 8 FUROS - PARA CHAPA DE 10MM', 'PINO-REI 3.1/2" 12 FUROS - PARA CHAPA DE 16MM', 'PINO-REI 3.1/2" 8 FUROS - PARA CHAPA DE 12MM']
    },
    {
        'nome': 'Engate de Contêiner',
        'modelos': ['ENGATE DE CONTÊINER - MODELO ANTERIOR', 'ENGATE DE CONTÊINER - MODELO 2014']
    },
    {
        'nome': 'Aparelho de Levantamento',
        'modelos': ['APARELHO DE LEVANTAMENTO B200G', 'APARELHO DE LEVANTAMENTO B200G TELESCÓPICO', 'APARELHO DE LEVANTAMENTO B200S', 'APARELHO DE LEVANTAMENTO B200T', 'APARELHO DE LEVANTAMENTO B280G', 'APARELHO DE LEVANTAMENTO B280S', 'APARELHO DE LEVANTAMENTO B280T']
    },
    {
        'nome': 'Engate Automático',
        'modelos': ['ENGATE AUTOMÁTICO [A PARTIR ANO 2019]', 'ENGATE AUTOMÁTICO [A PARTIR DE 2010 ATÉ 2018]', 'ENGATE AUTOMÁTICO [ATÉ 2009]']
    },
    {
        'nome': 'Ponteira',
        'modelos': ['PONTEIRA GIRATÓRIA - MODELOS LINHA', 'PONTEIRA GIRATÓRIA - MODELOS REPOSIÇÃO']
    },
    {
        'nome': 'Engate Esférico',
        'modelos': ['ENGATE ESFÉRICO [ANTERIORES]', 'ENGATE ESFÉRICO 90MM']
    },
    {
        'nome': 'Suspensor Pneumático Semirreboque',
        'modelos': ['SUSPENSOR PNEUMÁTICO AÇÃO DIRETA AÇÃO (MOLA "Z")', 'SUSPENSOR PNEUMÁTICO AÇÃO DIRETA PSYS', 'SUSPENSOR PNEUMÁTICO AÇÃO INDIRETA', 'SUSPENSOR PNEUMÁTICO FS250 - FIXAÇÃO M22', 'SUSPENSOR PNEUMÁTICO FS250 - FIXAÇÃO M30', 'SUSPENSOR PNEUMÁTICO FS250-09', 'SUSPENSOR PNEUMÁTICO PARA CHASSI DESLIZANTE', 'SUSPENSOR PNEUMÁTICO PARA SUSPENSÃO MECÂNICA']
    },
    {
        'nome': 'Suspensor Pneumático 3º Eixo',
        'modelos': ['SUSPENSOR PNEUMÁTICO - OUTROS MODELOS', 'SUSPENSOR PNEUMÁTICO AGRALE', 'SUSPENSOR PNEUMÁTICO FORD', 'SUSPENSOR PNEUMÁTICO INTERNATIONAL', 'SUSPENSOR PNEUMÁTICO IVECO', 'SUSPENSOR PNEUMÁTICO MAN', 'SUSPENSOR PNEUMÁTICO MERCEDES-BENZ', 'SUSPENSOR PNEUMÁTICO SCANIA', 'SUSPENSOR PNEUMÁTICO VOLKSWAGEN', 'SUSPENSOR PNEUMÁTICO VOLVO', 'SUSPENSOR PNEUMÁTICO VOLVO J-RIDE']
    },
    {
        'nome': 'Suspensor Pneumático Reposição',
        'modelos': ['SUSPENSOR PNEUMÁTICO REPOSIÇÃO']
    },
    {
        'nome': 'Porta Estepe',
        'modelos': ['PORTA ESTEPE INTERNATIONAL', 'PORTA ESTEPE FORD', 'PORTA ESTEPE IVECO - PE 275-180', 'PORTA ESTEPE IVECO - PE 335-250', 'PORTA ESTEPE MERCEDES-BENZ', 'PORTA ESTEPE MERCEDES-BENZ - LINHA LEVE', 'PORTA ESTEPE RANDON', 'PORTA ESTEPE VOLKSWAGEN']
    },
    {
        'nome': 'Hubodômetro',
        'modelos': ['HUBODÔMETRO']
    },
    {
        'nome': 'Rala',
        'modelos': ['RALA']
    },
     {
        'nome': 'Suporte Paralama Semirreboque',
        'modelos': ['SUPORTE PARALAMA SEMIRREBOQUE', 'SUPORTE PARALAMA SEMIRREBOQUE - REPOSIÇÃO']
    },
      {
        'nome': 'Kit para Veículo Trator',
        'modelos': ['FORD CARGO', 'FORD 4030', 'FORD 4331 MAXTON/ 4432 MAXTON UPGRADE', 'FORD 4532 MAXTON', 'INTERNATIONAL CONJUNTO KITS DE MONTAGEM', 'IVECO CAVALLINO/CURSOR/EUROCARGO/STRALIS/TECTOR', 'MAN TGX', 'MERCEDES-BENZ ACTROS', 'MERCEDES-BENZ ATEGO', 'MERCEDES-BENZ AXOR', 'MERCEDES-BENZ FSK 1938', 'MERCEDES-BENZ HSK 1938', 'MERCEDES-BENZ 1634', 'MERCEDES-BENZ 1723', 'MERCEDES-BENZ 1944', 'MERCEDES-BENZ 2638 CABINE ALONGADA', 'MERCEDES-BENZ 2638 CABINE SIMPLES', 'SCANIA - CONJUNTOS QUINTAS-RODAS JSK 37C', 'SCANIA - CONJUNTOS QUINTAS-RODAS REFORÇADAS', 'SCANIA LA 4X2 HZ COM 3º EIXO', 'VOLKSVAGEN 26.310 TITAN TRACTOR 6X4', 'VOLKSWAGEN - COMPONENTES DE MONTAGEM', 'VOLKSWAGEN CONSTELLATION 26.370 TRACTOR 6X4', 'VOLKSWAGEN 18.310 TITAN TRACTOR CABINE LEITO', 'VOLKSWAGEN 18.310 TITAN TRACTOR CABINE SIMPLES', 'VOLKSWAGEN 25.320E/25.370E/25.400E', 'VOLVO - CONJUNTO QUINTA-RODA']
    },
      {
        'nome': 'Enganche Automático - Mercado Externo',
        'modelos': ['ENGANCHE AUTOMATICO - A PARTIR DEL 2019', 'ENGANCHE AUTOMATICO - MODELO 2010', 'ENGANCHE AUTOMÁTICO - 1.1/2" (38MM) - HASTA 2009', 'ENGANCHE AUTOMÁTICO - 2" - HASTA 2009']
    },
      {
        'nome': 'Aro Giratorio - Mercado Externo',
        'modelos': ['ARO GIRATORIO']
    },
     {
        'nome': 'Enganche de Contenedor - Mercado Externo',
        'modelos': ['ENGATE DE CONTÊINER - MODELO 2014 [ME]']
    },
     {
        'nome': 'Levante Neumático - Mercado Externo',
        'modelos': ['LEVANTE NEUMÁTICO - CON COLUMNA [A PARTIR DEL 2019]', 'LEVANTE NEUMÁTICO - SIN COLUMNA [A PARTIR DEL 2019]', 'LEVANTE NEUMÁTICO - TRAVESSAÑO REBAJADO', 'LEVANTE NEUMÁTICO - TRAVESSAÑO RECTO']
    },
]

# Foi definido que a rota
# somente '/' traz o json completo
# '/itens/<id>' traz a informação de um item específico, conforme documentação
@app.route('/')
def MostrarTodosItens():
   return(jsonify(Itens))

@app.route('/itens/<int:id>')
def MostrarItensPorId(id):
   return(jsonify(Itens[id]))

#E verificado se o arquivo app.py está sendo executado pelo terminal 
# e, caso positivo, inicia o servidor do Flask
if __name__=="__main__":
    app.run(debug= True)