import logging
from pathlib import Path

LOG_PATH = Path("logs/app.log")

def get_logger():
    logger = logging.getLogger("app_logger")
    logger.setLevel(logging.INFO)

    # Ensure logs directory exists
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    # Avoid duplicate handlers in reloads/tests
    if not logger.handlers:
        handler = logging.FileHandler(LOG_PATH)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
