import logging
import allure
from utilities.baseClass import BaseClass


class AllureLoggingHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        with allure.step(log_entry):  # Adds log messages as steps in the Allure report
            pass


class CustomLogger:
    _instance = None

    def __new__(cls, level=logging.INFO):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logger = logging.getLogger('Selenium Automation')
            cls._instance.logger.setLevel(level)
            formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(lineno)d %(filename)s %(funcName)s]: %('
                                          'message)s',
                                          datefmt='%d%m%Y %I:%M:%S %p')

            log_file = BaseClass.ROOT_PATH + '/logs/' + 'logfile.log'

            # Add a file handler
            file_handler = logging.FileHandler(log_file, mode='w')
            file_handler.setLevel(level)
            file_handler.setFormatter(formatter)
            cls._instance.logger.addHandler(file_handler)

            # Add a console handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(level)
            console_handler.setFormatter(formatter)
            cls._instance.logger.addHandler(console_handler)

            # Add Allure logging handler
            allure_handler = AllureLoggingHandler()
            allure_handler.setLevel(level)
            allure_handler.setFormatter(formatter)
            cls._instance.logger.addHandler(allure_handler)

        return cls._instance

    def get_logger(self):
        return self.logger
