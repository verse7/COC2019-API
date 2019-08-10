import os
from flask import Flask

def create_api(test_config=None):
  api = Flask(__name__)

  if test_config is None:
    api.config.from_pyfile('config.py', silent=True)
  else:
    api.config.from_mapping(test_config)

  from api.model import db
  db.init_app(api)

  from api.form import csrf
  csrf.init_app(api)

  from api.view import auth
  api.register_blueprint(auth.bp)

  return api