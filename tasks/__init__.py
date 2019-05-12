
import tasks.narou.narou_tasks

def register_blueprints(app):
    app.register_blueprint(tasks.narou.narou_tasks.application)
