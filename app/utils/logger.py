import logging
from logging.handlers import RotatingFileHandler
import os
from flask import current_app, has_request_context, request

class RequestFormatter(logging.Formatter):
    """Formatter dengan info Flask request context."""

    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
            record.method = request.method
        else:
            record.url = None
            record.remote_addr = None
            record.method = None
        return super().format(record)

LOG_FORMAT = (
    "[%(asctime)s] %(levelname)s in %(module)s [%(process)d]: %(message)s"
    " | url=%(url)s remote_addr=%(remote_addr)s method=%(method)s"
)

def get_logger(name="app", config=None):
    """
    Ambil logger yang sudah terkonfigurasi sesuai config Flask app.
    :param name: Nama logger (modul)
    :param config: Flask config (app.config atau Config class, default: current_app.config)
    """
    logger = logging.getLogger(name)
    if logger.hasHandlers():
        return logger

    if config is None:
        try:
            config = current_app.config
        except Exception:
            config = {}

    LOG_LEVEL = str(config.get("LOG_LEVEL", os.getenv("LOG_LEVEL", "INFO"))).upper()
    LOG_DIR = config.get("LOG_DIR", os.getenv("LOG_DIR", "logs"))
    LOG_FILE = config.get("LOG_FILE", os.getenv("LOG_FILE", "app.log"))
    LOG_PATH = os.path.join(LOG_DIR, LOG_FILE)
    LOG_MAX_BYTES = int(config.get("LOG_MAX_BYTES", os.getenv("LOG_MAX_BYTES", 10 * 1024 * 1024)))
    LOG_BACKUP_COUNT = int(config.get("LOG_BACKUP_COUNT", os.getenv("LOG_BACKUP_COUNT", 5)))

    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR, exist_ok=True)

    formatter = RequestFormatter(LOG_FORMAT)

    file_handler = RotatingFileHandler(
        LOG_PATH, maxBytes=LOG_MAX_BYTES, backupCount=LOG_BACKUP_COUNT
    )
    file_handler.setLevel(LOG_LEVEL)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(LOG_LEVEL)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    logger.setLevel(LOG_LEVEL)
    logger.propagate = False

    return logger
