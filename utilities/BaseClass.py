import logging

import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        logger = logging.getLogger(__name__)

        # Proverite da li već postoji file_handler
        file_handler_exists = any(isinstance(handler, logging.FileHandler) for handler in logger.handlers)

        if not file_handler_exists:
            file_handler = logging.FileHandler("logFILE.log", encoding='utf-8')
            logger.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger


