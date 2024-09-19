# Introduction

Challenge of creating an API in Python using Flask.

# API

The API created returns data from models of items in the Jost company catalog, available at the link: http://catalogo.jost.com.br/

The information was input into the code through a list of dictionaries that contain the name of the part and the available models. In order to be able to return a JSON with the information present in the dictionary, the jsonify library was used (in the example below, the list of items is stored in the "Items" variable and the API return is in the default route).
```
@app.route('/')
def MostrarTodosItens():
   return(jsonify(Itens))
```

To run the Python code, simply run the following command in the terminal: set FLASK_APP=app and then flask run.

To access the entire catalog in JSON format, simply access the default route (the link appears as output from *flask run*). To access the models of a specific part, simply access the default route by adding /items/<id_part>.

The id of each item in the catalog is as follows:

| id | Part |
| ------------- | ------------- |
| 0 | Fifth-wheel |
| 1 | Fifth-wheel table |
| 2 | Kingpin |
| 3 | Container hitch |
| 4 | Lifting device |
| 5 | Automatic hitch |
| 6 | Tipper |
| 7 | Ball hitch |
| 8 | Semi-trailer pneumatic suspension |
| 9 | 3rd axle pneumatic suspension |
| 10 | Replacement Air Suspension |
| 11 | Spare Tire Holder |
| 12 | Hubodometer |
| 13 | Rala |
| 14 | Semi-trailer Fender Support |
| 15 | Tractor Vehicle Kit |
| 16 | Automatic Hitch - Foreign Market |
| 17 | Swivel Ring - Foreign Market |
| 18 | Container Hitch - Foreign Market |
| 19 | Pneumatic Lift - Foreign Market |
