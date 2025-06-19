from flask import Flask
from .post_controller import bp as post_bp
from .check_controller import bp as check_bp

def register_routes(app: Flask):
    API_PREFIX = "/api/v1"
    app.register_blueprint(post_bp, url_prefix=f"{API_PREFIX}/posts")
    app.register_blueprint(check_bp, url_prefix=f"{API_PREFIX}/check")
