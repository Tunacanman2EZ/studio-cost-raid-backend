from flask import Flask
from config import config_map  # explanation - brings in the map of env name -> config class
from .extensions import db, migrate   # import the helper objects you made
from .main import main_bp               # import the blueprint you just made
from dotenv import load_dotenv  # explanation - function that loads variables from .env into the environment
import os                       # explanation - lets us access environment variables via os.environ

load_dotenv()  # explanation - read key=value pairs from .env and add them to environment variables

def create_app(config_name="development"):   # config_name has a default value now
    app = Flask(__name__)                         # create the Flask app object 
    
    config_class = config_map[config_name]  # explanation - pick the right config class based on the config_name string
    app.config.from_object(config_class)    # explanation - copy all uppercase attributes from the config class into app.config
    print(
        "CURRENT CONFIG:",
        app.config.get("SQLALCHEMY_DATABASE_URI"),
        app.config.get("JWT_SECRET_KEY")
    )  # explanation - show which DB URL and JWT secret the app loaded from config/env
    print("CURRENT CONFIG:", app.config.get("SQLALCHEMY_DATABASE_URI"), app.config.get("JWT_SECRET_KEY")[:5])
    # explanation - debug print to show which DB URL and first chars of JWT secret are loaded

    db.init_app(app)                              # connect the db helper to this app
    migrate.init_app(app, db)                     # connect migrations to this app + db
    app.register_blueprint(main_bp)     # attach the main blueprint to the app

    return app                                    # give the configured app back