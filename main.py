#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" main.py


"""

from flask import Flask

import kushimori
import tasks
import users

import utils.config

def build_app():
    app = Flask(__name__)
    kushimori.register_blueprints(app)
    tasks.register_blueprints(app)
    users.register_blueprints(app)
    
    return app

def main():    
    app.run(host='0.0.0.0', port=8080, debug=True)


utils.config.load_config()

app = build_app()

if __name__ == "__main__":
    main()
