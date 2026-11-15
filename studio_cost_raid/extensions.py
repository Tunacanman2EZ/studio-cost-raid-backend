from flask_sqlalchemy import SQLAlchemy   # get the SQLAlchemy class from the flask_sqlalchemy package
from flask_migrate import Migrate        # get the Migrate class from the flask_migrate package

db = SQLAlchemy()                        # create a db helper object, not linked to any app yet
migrate = Migrate()                      # create a migrate helper object, not linked to any app yet