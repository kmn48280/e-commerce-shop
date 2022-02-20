from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask_login import LoginManager
# from flask_moment import Moment

# init my Login Manager 
login = LoginManager()

# Do inits for database stuff 
db = SQLAlchemy()
migrate = Migrate()
# moment = Moment()

def create_app(config_class=Config):
    #init the app
    app = Flask(__name__)

    #link our config to our app
    app.config.from_object(config_class)

    # register plugins 
    login.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    #This is where you will be sent if you are not logged
    # into FIXME trying to go to a login required page
    # TODO!!!!!
    login.login_view='auth.login'
    login.login_message = 'Log in to view content'
    login.login_message_category = 'warning'

    # moment.init_app(app)

    from .blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from .blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)

    from .blueprints.shop import bp as shop_bp
    app.register_blueprint(shop_bp)


    return app

