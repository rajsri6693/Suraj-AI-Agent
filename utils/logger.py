import logging
import os

from datetime import datetime


class Logger:

    def __init__(self, name="SurajAI"):

        os.makedirs("logs", exist_ok=True)

        today = datetime.now().strftime("%Y-%m-%d")

        logfile = f"logs/{today}.log"

        self.logger = logging.getLogger(name)

        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:

            file_handler = logging.FileHandler(
                logfile,
                encoding="utf-8"
            )

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"
            )

            file_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)

    def info(self, message):

        print(message)

        self.logger.info(message)

    def error(self, message):

        print(message)

        self.logger.error(message)

    def exception(self, message):

        print(message)

        self.logger.exception(message)