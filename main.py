#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" main.py


"""

from flask import Flask

import tasks

def build_app():
    app = Flask(__name__)
    tasks.register_blueprints(app)

    return app

app = build_app()
    
@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

def main():
    app.run(host='0.0.0.0', port=8080, debug=True)



if __name__ == "__main__":
    main()
