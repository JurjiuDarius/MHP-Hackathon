from flask import Flask
from controller import blueprints
from flask_migrate import Migrate
from database import db
from flask_cors import CORS
from dotenv import load_dotenv
from models.migrations.init_db import add_all_to_database
from sqlalchemy import text
import os
import models


def create_app():

    if os.path.exists("/.dockerenv"):
        load_dotenv(override=False)
    else:
        load_dotenv(override=True)

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

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument(
        "-p", "--port", default=5000, type=int, help="port to listen on"
    )
    CERT_FILE = app.config.get("CERT_LOCATION", "cert.pem")
    KEY_FILE = app.config.get("KEY_LOCATION", "key.pem")
    with app.app_context():
        add_all_to_database()
        with db.engine.connect() as connection:
            connection.execute(text("SET datestyle = 'ISO, MDY';"))

    args = parser.parse_args()
    port = args.port
    os.system("flask db upgrade")
    app.run(host="0.0.0.0", port=port, ssl_context=(CERT_FILE, KEY_FILE))
