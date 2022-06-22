
from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS


# routes
from routes.auth.auth import routes_auth
from routes.aplicativos.aplicativos import application
from routes.area.area import area
from routes.estado.estado import estado
from routes.usuarios.usuarios import users
from routes.modulo.modulo import modulos
from routes.Transacciones.Transacciones import transactions
from routes.tipo.tipo import tipo
from routes.sap_knowledge.sap_knowledge import sap


# from flask_sqlalchemy import SQLAlchemy
# from config import DATABASE_CONNECTION_URI


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# settings
app.secret_key = 'mysecret'
# print(DATABASE_CONNECTION_URI)
# app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# SQLAlchemy(app)

app.register_blueprint(routes_auth, url_prefix='/api')
app.register_blueprint(application, url_prefix='/aplicativos')
app.register_blueprint(users, url_prefix='/usuarios')
app.register_blueprint(modulos, url_prefix='/modulos')
app.register_blueprint(transactions, url_prefix='/Tx')
app.register_blueprint(tipo, url_prefix='/tipo')
app.register_blueprint(area, url_prefix='/area')
app.register_blueprint(estado, url_prefix='/estado')
app.register_blueprint(sap, url_prefix='/sap')

if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True, port="4000",host="0.0.0.0")