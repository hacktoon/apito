# coding: utf-8

import sys
import logging


class Log:
    def __init__(self, name):
        self._logger = logging.getLogger(name)
        if len(self._logger.handlers):
            return
        consoleHandler = logging.StreamHandler(sys.stdout)
        consoleHandler.setFormatter(self._build_log_format())
        self._logger.setLevel(logging.INFO)
        self._logger.addHandler(consoleHandler)
        self._logger.propagate = False

    def _build_log_format(self):
        date_fmt = "%d/%m/%Y %H:%M:%S"
        fmt_string = '%(name)s:%(levelname)s | %(asctime)s | %(message)s'
        return logging.Formatter(fmt_string, date_fmt)

    def info(self, message):
        self._logger.info(message)

    def error(self, message):
        self._logger.error(message)
