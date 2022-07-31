from flask import Flask

def create_app():
    app = Flask(_name_)
    app.config['SECRET_KEY'] = 'Aa'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
