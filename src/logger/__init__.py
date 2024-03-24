import logging
import os

from from_root import from_root
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"
LOG_DIR = 'logs'

logpath = os.path.join(from_root(),LOG_DIR,LOG_FILE)

os.makedirs(LOG_DIR, exist_ok=True)


logging.basicConfig(
    filename=logpath,
    format="%(levelname)s - %(asctime)s - %(message)s - %(name)s",
    level=logging.DEBUG)
print(logpath)