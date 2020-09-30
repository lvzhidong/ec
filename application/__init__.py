# coding: u8

from __future__ import unicode_literals
import os
import logging
from flask import Flask
from application.models import db


def create_app():
    app = Flask(__name__)
    _init_config(app)
    # _init_database(app)
    _init_admin(app)
    return app


def _init_config(app):
    env = os.environ.get('ENV', 'default')
    if env == 'default':
        from config_default import Config
    elif env == 'product':
        from config_product import Config
    app.config.from_object(Config)
    logging.basicConfig(
        level=logging.DEBUG if app.config.get('DEBUG', False) else logging.INFO,
        format='%(asctime)s|%(levelname)s|%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )


def _init_database(app):
    db.init_app(app)


def _init_admin(app):
    import application.views as adminviews
    from application import views
    from flask_admin import Admin
    admin = Admin(app, name='EC backend')
    admin.add_views(views.SqlGenView(), )

