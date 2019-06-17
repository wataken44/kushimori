
import dashboard.views

def register_blueprints(app):
    app.register_blueprint(dashboard.views.application)
