
import tasks.narou.narou_tasks
import tasks.sample

def register_blueprints(app):
    app.register_blueprint(tasks.narou.narou_tasks.application)
    app.register_blueprint(tasks.sample.application)
