import logging


class Logger:
    def getLogger(self):
        LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
        logging.basicConfig(filename="QuestionFour.log", level=logging.DEBUG, format=LOG_FORMAT)
        logger = logging.getLogger()

        return logger
