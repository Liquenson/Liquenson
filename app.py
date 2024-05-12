from flask import Flask

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Definir una ruta y la función que manejará esa ruta
@app.route('/')
def index():
    return '¡Hola mundo! Esta es mi primera página web con Flask.'

# Ejecutar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
