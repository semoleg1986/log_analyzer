import logging
from logging.handlers import RotatingFileHandler

from core.constants import LOG_FILE, LOGS_DIR

LOGS_DIR.mkdir(parents=True, exist_ok=True)


def get_logger(name: str) -> logging.Logger:
    """
    Настраивает и возвращает логгер с именем `name`.
    Логирует в файл.

    :param name: имя логгера
    :return: logging.Logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.hasHandlers():
        file_handler = RotatingFileHandler(
            LOG_FILE, maxBytes=1024 * 1024, backupCount=5, encoding="utf-8"
        )
        file_handler.setLevel(logging.INFO)
        file_formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        )
        file_handler.setFormatter(file_formatter)

        logger.addHandler(file_handler)

    return logger
