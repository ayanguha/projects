
from flask import Flask,request,Response,jsonify,Blueprint

from flask_sqlalchemy import SQLAlchemy

import settings
from api.endpoints.data import artefact_ns,foundation_ns,audit_ns

from api.endpoints.data import api
from api.handlers.handlers import db

app = Flask(__name__)

def configure_app(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def initialize_app(flask_app):
    configure_app(flask_app)
    blueprint = Blueprint('api', __name__)
    api.init_app(blueprint)
    api.add_namespace(artefact_ns)
    api.add_namespace(foundation_ns)
    api.add_namespace(audit_ns)
    flask_app.register_blueprint(blueprint)
    db.app = flask_app
    db.init_app(flask_app)


initialize_app(app)


def main():

    app.run(debug=settings.FLASK_DEBUG,port=5010)

if __name__ == "__main__":
    main()
