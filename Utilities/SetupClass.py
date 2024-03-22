import logging
import os
import sys

from selenium.common import WebDriverException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from Constans import where_to_send
from Logs import LogClass


class SetupClass(LogClass):
    path: str
    driver: WebDriver
    wait: WebDriverWait
    log: logging.Logger
    action: ActionChains

    def __init__(self, which_driver):
        self.path = os.getcwd()
        self.log = self.get_logger()
        self.log.info("working dir: " + self.path)
        self.driver = self.__get_driver(which_driver)
        self.wait = WebDriverWait(self.driver, timeout=10)
        self.action = ActionChains(self.driver)

    def __get_driver(self, which_driver):
        match which_driver:
            case 0:
                try:
                    service_obj = Service(executable_path=self.path + r"\chromedriver.exe")
                    driver = webdriver.Chrome(service=service_obj)
                    self.log.info("connected to chrome successfully")
                    return driver
                except FileNotFoundError:
                    self.log.info(f"Chrome driver not found at: {self.path}. Trying to connect to other drivers")
                except WebDriverException as e:
                    self.log.critical(f"Error initializing Chrome driver. Error: {e}")
                except Exception as e:
                    self.log.critical(f"An unexpected error occurred with chrome: {e}")

            case 1:
                try:
                    service_obj = Service(executable_path=self.path + r"\geckodriver.exe")
                    driver = webdriver.Firefox(service=service_obj)
                    self.log.info("connected to Firefox successfully")
                    return driver
                except FileNotFoundError:
                    self.log.info(f"Mozilla driver not found at: {self.path}. Trying to connect to other driver")
                except WebDriverException as e:
                    self.log.critical(f"Error initializing Mozilla driver. Error: {e}")
                except Exception as e:
                    self.log.critical(f"An unexpected error occurred with Mozilla: {e}")

            case 2:
                try:
                    service_obj = Service(executable_path=self.path + r"\msedgedriver.exe")
                    driver = webdriver.Edge(service=service_obj)
                    self.log.info("connected to Edge successfully")
                    return driver
                except FileNotFoundError as e:
                    self.log.critical(
                        f"Couldn't connect to any driver. Edge driver not found at: {self.path}. Error: {e}")
                except WebDriverException as e:
                    self.log.critical(f"Error initializing Edge driver. Error: {e}")
                except Exception as e:
                    self.log.critical(f"An unexpected error occurred with Edge: {e}")
            case _:
                self.log.critical("Didn't select proper driver")

    def setup_receiver_email(self):
        if len(sys.argv) > 1:
            receiver_email = sys.argv[1]
            self.log.info(f"user inputted his mail {receiver_email}")
        else:
            receiver_email = where_to_send.EMAIL_TO_RECIVE_INFO
            self.log.info(f"used email from the file which is {receiver_email}")
        return receiver_email
