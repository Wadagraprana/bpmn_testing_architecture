import logging
import os
from logging.handlers import RotatingFileHandler

try:
    from flask import current_app, has_request_context, request
except ImportError:
    current_app = None

    def has_request_context():
        return False

    request = None


class RequestFormatter(logging.Formatter):
    """Formatter dengan info Flask request context."""

    def format(self, record):
        if has_request_context():
            record.url = getattr(request, "url", None)
            record.remote_addr = getattr(request, "remote_addr", None)
            record.method = getattr(request, "method", None)
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
    Return a configured logger for the app/module.
    :param name: Logger name.
    :param config: Flask config dict/class, or None.
    """
    logger = logging.getLogger(name)

    # Remove all handlers to avoid duplicate logs if logger is reinitialized
    if logger.hasHandlers():
        logger.handlers.clear()

    # Load config, with Flask or env fallback
    if config is None:
        try:
            config = current_app.config
        except Exception:
            config = {}

    LOG_LEVEL = str(config.get("LOG_LEVEL", os.getenv("LOG_LEVEL", "INFO"))).upper()
    LOG_DIR = config.get("LOG_DIR", os.getenv("LOG_DIR", "logs"))
    LOG_FILE = config.get("LOG_FILE", os.getenv("LOG_FILE", "app.log"))
    LOG_PATH = os.path.join(LOG_DIR, LOG_FILE)
    LOG_MAX_BYTES = int(
        config.get("LOG_MAX_BYTES", os.getenv("LOG_MAX_BYTES", 10 * 1024 * 1024))
    )
    LOG_BACKUP_COUNT = int(
        config.get("LOG_BACKUP_COUNT", os.getenv("LOG_BACKUP_COUNT", 5))
    )

    # Make sure log dir exists
    os.makedirs(LOG_DIR, exist_ok=True)

    formatter = RequestFormatter(LOG_FORMAT)

    # Add Rotating File Handler (safe fallback if file permission issue)
    try:
        file_handler = RotatingFileHandler(
            LOG_PATH, maxBytes=LOG_MAX_BYTES, backupCount=LOG_BACKUP_COUNT
        )
        file_handler.setLevel(LOG_LEVEL)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    except Exception as e:
        # Fallback: log error only to console if file handler fails
        print(f"[LOGGER INIT] Could not add file handler: {e}")

    console_handler = logging.StreamHandler()
    console_handler.setLevel(LOG_LEVEL)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    logger.setLevel(LOG_LEVEL)
    logger.propagate = False

    return logger
