import os
from app.logger import get_logger, LOG_PATH

def test_logging_creates_file():
    logger = get_logger()
    logger.info("test log entry")
    assert os.path.exists(LOG_PATH)
