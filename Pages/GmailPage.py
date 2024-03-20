import csv
import json
import os

from datetime import date
from Constans import uri, element_tuples, arrays
from selenium.webdriver.support import expected_conditions as EC


class GmailPage:

    def __init__(self, driver, wait, log, action, receiver, sender_email, sender_password):

        self.driver = driver
        self.wait = wait
        self.log = log
        self.action = action
        self.receiver = receiver
        self.sender_email = sender_email
        self.sender_password = sender_password

    def exit_script(self):
        self.driver.quit()
        os._exit(0)

    def open_gmail(self):
        try:
            self.driver.get(uri.MAIL_URL)
        except:
            self.log.error("Failed to open new web tab")
            self.exit_script()

    def log_in_gmail(self):
        self.driver.find_element(*element_tuples.GMAIL_LOGIN_MAIL_INPUT).send_keys(self.sender_email)
        self.driver.find_element(*element_tuples.GMAIL_SUBMIT_MAIL_BUTTON).click()
        self.wait.until(EC.visibility_of_element_located(element_tuples.GMAIL_LOGIN_PASSWORD_INPUT))
        self.driver.find_element(*element_tuples.GMAIL_LOGIN_PASSWORD_INPUT).send_keys(self.sender_password)
        self.wait.until(EC.element_to_be_clickable(element_tuples.GMAIL_SUBMIT_MAIL_BUTTON))
        self.driver.find_element(*element_tuples.GMAIL_SUBMIT_MAIL_BUTTON).click()

    def create_new_mail(self):
        try:
            self.driver.find_element(*element_tuples.GMAIL_CREATE_NEW_LETTER_BUTTON).click()
            self.log.info("Logged into gmail successfully")
        except:
            self.log.error("Failed to log into gmail")
            self.exit_script()

    def excel_to_json(self):
        gas_data = {}
        for prices in arrays.EXCEL_NAMES:
            with (open(prices, mode="r", newline='', encoding='UTF-8') as csvfile):
                reader = csv.reader(csvfile)
                rows_read = 0
                gas_data[prices.split(".")[0]] = []
                for row in reader:
                    if rows_read == 5:
                        break
                    if row[0] == "adresai":
                        continue
                    gas_data[prices.split(".")[0]].append({"adresas": row[0], "kaina": row[1]})
                    rows_read += 1
                if not gas_data:
                    self.log.error("Failed to convert excel to json")
                    self.exit_script()
                with open("json_file.json", mode="w", encoding='UTF-8') as json_file:
                    json.dump(gas_data, json_file, indent=4, ensure_ascii=False)

    def get_list_from_json_lowest_price(self):
        self.excel_to_json()
        with open('json_file.json', mode="r", encoding='UTF-8') as json_file:
            all_prices = json.load(json_file)
        lowest_prices = []
        for gas in all_prices:
            found_station = False
            for station in lowest_prices:
                if all_prices[gas][0]['adresas'] == station[0]:
                    found_station = True
                    station.append(str(gas))
                    station.append("- " + all_prices[gas][0]['kaina'])
                    break
            if not found_station:
                new_array = [all_prices[gas][0]['adresas'], gas, ("- " + all_prices[gas][0]['kaina'])]
                lowest_prices.append(new_array)
        return lowest_prices

    def get_letter_content(self):
        list_with_prices = self.get_list_from_json_lowest_price()
        letter_content = ""
        for list_line in list_with_prices:
            for variables in list_line:
                letter_content += (variables + " ")
            letter_content += "\n"
        if not letter_content:
            self.log.error("Couldn't collect information into letter_content array")
            self.exit_script()
        return letter_content

    def fill_and_send_mail_using_selenium(self):
        self.driver.implicitly_wait(4)
        try:
            self.driver.find_element(*element_tuples.GMAIL_MAIL_RECIEVER).send_keys(self.receiver)
        except:
            self.driver.find_element(*element_tuples.GMAIL_MAIL_TO_RECIEVER).send_keys(self.receiver)
        self.driver.find_element(*element_tuples.GMAIL_MAIL_SUBJECT).send_keys(str(date.today()) + " gas report")
        self.driver.find_element(*element_tuples.GMAIL_MAIL_CONTENT).send_keys(self.get_letter_content())
        self.driver.find_element(*element_tuples.GMAIL_MAIL_SEND_BUTTON).click()
        try:
            self.wait.until(EC.presence_of_element_located(element_tuples.GMAIL_SUCCESS_POPUP))
            self.log.info("email send successfully")
        except:
            self.log.error("Didn't send the email")
            self.exit_script()
