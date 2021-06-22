# -*- coding: utf-8 -*-


import os
import logging
from logging import StreamHandler, FileHandler
from logging.handlers import TimedRotatingFileHandler


def generator_logging(log_path):
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fHandler = TimedRotatingFileHandler(log_path, when="MIDNIGHT", backupCount=10)
    fHandler.setLevel(logging.INFO)
    fHandler.setFormatter(formatter)
    logger.addHandler(fHandler)
    sHandler = StreamHandler()
    sHandler.setLevel(logging.INFO)
    sHandler.setFormatter(formatter)
    logger.addHandler(sHandler)
    return logger