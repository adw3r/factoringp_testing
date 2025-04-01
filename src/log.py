import sys
from loguru import logger

from src.config import ROOT_DIR

logger.remove()
LOGGING_FORMAT = (
    "<level>{time:YYYY-MM-DD HH:mm:ss.SSS}</level> "
    "<level>{level}</level>: "
    "<level>{name}</level> - "
    "<level>{message}</level>"
)

logger.add(
    ROOT_DIR / "logs" / "log_{time:YYYY-MM-DD}.log",
    format=LOGGING_FORMAT,
    level="DEBUG",
    mode="a",
    retention="5 days",
)
logger.add(sys.stdout, format=LOGGING_FORMAT)
