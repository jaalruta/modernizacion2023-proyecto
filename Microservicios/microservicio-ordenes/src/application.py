import os



from flask import Flask
from flask import abort
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api
from modelos import db
from vistas import VistaOrdenes, VistaObtenerOrdenes , VistaPing

USER = "postgres" if os.getenv('DB_USER') is None else os.getenv('DB_USER')
PASSWORD = "postgres" if os.getenv('DB_PASSWORD') is None else os.getenv('DB_PASSWORD')
HOST = "modernizacion.cdaclc8hov9i.us-east-1.rds.amazonaws.com" if os.getenv('DB_HOST') is None else os.getenv('DB_HOST')
DB = "modernizacion" if os.getenv('DB_NAME') is None else os.getenv('DB_NAME')
PORT = "5432" if os.getenv('DB_PORT') is None else os.getenv('DB_PORT')


DB_HOST = HOST+":"+PORT
basedir = os.path.abspath(os.path.dirname(__file__))
application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://'+USER+':'+PASSWORD+'@'+DB_HOST+'/'+DB
application.config['JWT_SECRET_KEY'] = 'frase-secreta'
application.config['PROPAGATE_EXCEPTIONS'] = True

app_context = application.app_context()
app_context.push()

db.init_app(application)
db.create_all()

cors = CORS(application)

api = Api(application)


api.add_resource(VistaOrdenes, '/orden')
api.add_resource(VistaObtenerOrdenes, '/orden/<u_id>')
api.add_resource(VistaPing, '/orden/ping')
app = application

if __name__ == "__main__":
    application.run(port = 5000, debug = True)