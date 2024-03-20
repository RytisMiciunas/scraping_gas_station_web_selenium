import os
import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from Constans import uri
from Pages.GmailPage import GmailPage
from Pages.LandingPage import LandingPage
from Utilities.SetupClass import SetupClass


class BaseClass(SetupClass):
    path: str
    driver: WebDriver
    wait: WebDriverWait
    log: logging.Logger
    action: ActionChains
    receiver_email: str

    landing_page: LandingPage
    gmail_page: GmailPage

    def __init__(self, which_driver):
        super(BaseClass, self).__init__(which_driver)
        self.driver.get(uri.WEB_URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.landing_page = LandingPage(self.driver, self.wait, self.log)
        self.gmail_page = GmailPage(self.driver, self.wait, self.log, self.action, self.setup_receiver_email(),
                                    os.getenv('USER_MAIL'), os.getenv('USER_PASW'))

    def close_web(self):
        self.driver.quit()

    def close_logger(self):
        handlers = self.log.handlers[:]
        for handler in handlers:
            self.log.removeHandler(handler)
            handler.close()
