import logging
import os
from datetime import datetime

LOGS_DIR = "logs"
os.makedirs(LOGS_DIR,exist_ok=True)

LOG_FILE = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")

logging.basicConfig(
    filename=LOG_FILE,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO# there  are many levels but only warning info and error will be shown
)

def get_logger(name): # functrion used to initialise logger in different files
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger
