import pytest
import logging
import inspect

#using fixture setup
@pytest.mark.usefixtures("setup")
class BaseClass:
    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        # createloggerwith'spam_application'
        logger = logging.getLogger(loggerName)
        # createfilehandlerwhichlogsevendebugmessages
        fileHandler = logging.FileHandler('/Users/vasanp/PycharmProjects/pythonProject/selenium_mainassignment/Logs/logfile.log')
        # createformatterandaddittothehandlers
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(name)s-%(funcName)s-%(message)s')
        fileHandler.setFormatter(formatter)
        # addthehandlerstothelogger
        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)

        return logger
