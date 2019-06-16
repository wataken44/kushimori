
import users.views

def register_blueprints(app):
    app.register_blueprint(users.views.application)
