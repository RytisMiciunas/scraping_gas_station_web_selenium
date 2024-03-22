import inspect
import logging


class LogClass:
    logger = ""

    def get_logger(self):
        if self.logger == "":
            self.logger = self.__create_logger()
            return self.logger
        else:
            return self.logger

    def __create_logger(self):
        logger_handler = logging.getLogger(inspect.stack()[2][3])  # telling from where log came

        file_handler = logging.FileHandler('log_file.log', encoding='UTF-8')     # erase 'w' if dont want reset log file everytime
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s")
        file_handler.setFormatter(formatter)

        logger_handler.addHandler(file_handler)
        logger_handler.setLevel(logging.DEBUG)  # change if you don't want to see all logs from DEBUG level
        return logger_handler



