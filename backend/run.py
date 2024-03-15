from flask import Flask
from controller import blueprints
from flask_migrate import Migrate
from database import db
from flask_cors import CORS
from OpenSSL import SSL
from dotenv import load_dotenv
import os
import models


def create_ssl_context(cert_location, key_location):
    context = SSL.Context(SSL.PROTOCOL_TLSv1_2)
    context.use_privatekey_file(cert_location)
    context.use_certificate_file(key_location)


def create_app():
    load_dotenv()
    app = Flask(__name__)
    env_config = os.getenv("APP_SETTINGS")
    app.config.from_object(env_config)
    db.init_app(app)
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
    CORS(app, allow_headers="*", expose_headers="*")
    return app


app = create_app()

migrate = Migrate(
    app,
    db,
    directory=app.config.get("MIGRATIONS_DIR", "./migrations"),
)
migrate.init_app(app, db)

print("Working")
if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument(
        "-p", "--port", default=5000, type=int, help="port to listen on"
    )
    CERT_FILE = app.config.get("CERT_LOCATION", "cert.pem")
    KEY_FILE = app.config.get("KEY_LOCATION", "key.pem")

    args = parser.parse_args()
    port = args.port

    app.run(host="127.0.0.1", port=port, ssl_context=(CERT_FILE, KEY_FILE))
