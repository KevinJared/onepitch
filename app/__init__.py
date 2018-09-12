from flask import Flask
from config import CONFIG_OPTIONS
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_simplemde import SimpleMDE
from flask_mail import Mail
from flask_uploads import UploadSet,configure_uploads,IMAGES

simple = SimpleMDE()
bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
photos = UploadSet('photos',IMAGES)

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(CONFIG_OPTIONS[config_name])

    # configure UploadSet
    configure_uploads(app,photos)

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    simple.init_app(app)
    mail.init_app(app)


    # Registering th blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,prefix='/authenticate')
    return app
