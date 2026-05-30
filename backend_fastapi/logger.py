import os
import logging

from logging.handlers import RotatingFileHandler

# Create logs directory automatically
os.makedirs("logs", exist_ok=True)

# Create logger
logger = logging.getLogger("medrag_logger")

logger.setLevel(logging.INFO)

# File handler
file_handler = RotatingFileHandler(
    "logs/app.log",
    maxBytes=1024 * 1024,
    backupCount=5
)

# Log format
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

file_handler.setFormatter(formatter)

# Add handler
logger.addHandler(file_handler)