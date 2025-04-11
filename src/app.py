from flask import Flask
from flask_cors import CORS
from config.config import app_config

from apis.empleados.routes import Empleados
from apis.hoteles.routes import Hoteles
from apis.limpiezas.routes import Limpiezas
from apis.pagos.routes import Pagos
from apis.reservas.routes import Reservas
from apis.serviciosadicionales.routes import ServiciosAdicionales
from apis.clientes.routes import Clientes

#Crear una instancia de la aplicacion flask 
app = Flask(__name__)

#Habilitar CORS para todas las rutas y origenes
#Esto permite que el frontend realice solitudes a la API
CORS(app)

#Definir un manejador de errores para rutas no encontradas
def paginaNoEncontrada(error):
    return "<h1>Página no encontrada</h1>", 404

def errorServidor(error):
    return "<h1>Error intero del servidor</h1>", 500

@app.route('/')
def principal():
    return "<h1>Bienvenido a mi aplicacion con Falsk</h1>"

if __name__ == '__main__':
    #Cargamos las configuracion para el entorno 'development'
    app.config.from_object(app_config['development'])

    app.register_blueprint(Empleados.main, url_prefix="/api/empleados")
    app.register_blueprint(Hoteles.main, url_prefix="/api/hoteles")
    app.register_blueprint(Limpiezas.main, url_prefix="/api/limpiezas")
    app.register_blueprint(Pagos.main, url_prefix="/api/pagos")
    app.register_blueprint(Reservas.main, url_prefix="/api/reservas")
    app.register_blueprint(ServiciosAdicionales.main, url_prefix="/api/serviciosadicionales")
    app.register_blueprint(Clientes.main, url_prefix="/api/clientes")

    #Registramos el manejador de error 404
    app.register_error_handler(404, paginaNoEncontrada)
    app.register_error_handler(500, errorServidor)

    #Iniciamos el servidor de flask, escuchando en el puerto 5000.
    app.run(host='0.0.0.0', port=5000, debug=True)

