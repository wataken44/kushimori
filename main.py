#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" main.py


"""

from flask import Flask

import tasks
import kushimori

def build_app():
    app = Flask(__name__)
    kushimori.register_blueprints(app)
    tasks.register_blueprints(app)

    return app

app = build_app()
    
def main():
    app.run(host='0.0.0.0', port=8080, debug=True)

if __name__ == "__main__":
    main()
