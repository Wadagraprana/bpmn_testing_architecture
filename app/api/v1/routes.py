from flask import Flask

from .post_controller import bp as post_bp


def register_routes(app: Flask):
    app.register_blueprint(post_bp)
