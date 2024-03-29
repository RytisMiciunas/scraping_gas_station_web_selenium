import csv
import sys
import requests

from bs4 import BeautifulSoup
from Constans import element_tuples, uri, arrays
from selenium.webdriver.support import expected_conditions as EC


class LandingPage:
    scraped_array = []

    def __init__(self, driver, wait, log):

        self.driver = driver
        self.wait = wait
        self.log = log

    def exit_script(self):
        self.driver.quit()
        sys.exit(1)

    def change_language(self):
        self.wait.until(
            EC.element_to_be_clickable(element_tuples.LT_LANGUAGE_BUTTON)).click()
        if uri.LT_LANGUAGE_IN_URL in self.driver.current_url:
            self.log.info("changed to LT language successfully")
        else:
            self.log.error("didn't change to LT language")
            self.exit_script()

    def choose_city(self):
        try:
            self.driver.find_element(*element_tuples.CITIES_DROPBOX).click()
            self.driver.find_element(*element_tuples.VILNIUS_OPTION_IN_DROPBOX).click()
            self.log.info("selected Vilnius successfully")
        except Exception as e:
            self.log.error(f"couldn't select Vilnius. error: {e}")
            self.exit_script()

    def sort_array(self, gas_index):
        try:
            self.scraped_array = sorted(self.scraped_array, key=lambda tup: tup[gas_index])
        except Exception as e:
            self.log.error(f"Couldn't sort properly {gas_index}. error: {e}")

    def create_excels(self):
        delimiter = ","
        fieldnames = ["adresai", "kaina"]
        for index, excel_name in enumerate(arrays.EXCEL_NAMES, start=1):
            self.sort_array(index)
            with open(excel_name, "w", encoding='UTF-8', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=delimiter)
                writer.writeheader()
                for items in self.scraped_array:
                    writer.writerow({'adresai': items[0], 'kaina': items[index]})

    def scrap_content(self):
        r = requests.get(self.driver.current_url)
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find_all('td')
        index = 0
        if len(table) == 0:
            self.log.error("Didn't scrap information from web")
        while index < len(table):
            gas_station_name = table[index].text
            gas_station_name = gas_station_name.splitlines()[1]
            dyzel = table[index + 1].text
            if dyzel == "-":
                dyzel = "empty"
            ninty_five = table[index + 2].text
            if ninty_five == "-":
                ninty_five = "empty"
            ninty_eight = table[index + 3].text
            if ninty_eight == "-":
                ninty_eight = "empty"
            lpg = table[index + 4].text
            if lpg == "-":
                lpg = "empty"
            new_tuple = (gas_station_name, dyzel, ninty_five, ninty_eight, lpg)
            self.scraped_array += (new_tuple,)
            index += 5

        self.create_excels()

    def open_new_tab(self):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
