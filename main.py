import os
import time

from Utilities.BaseClass import BaseClass
from dotenv import load_dotenv


def main():
    setup()
    for index in range(3):
        main_obj = BaseClass(index)
        main_obj.landing_page.change_language()
        main_obj.landing_page.choose_city()
        main_obj.landing_page.scrap_content()
        main_obj.landing_page.open_new_tab()
        main_obj.gmail_page.open_gmail()
        main_obj.gmail_page.log_in_gmail()
        main_obj.gmail_page.create_new_mail()
        # time.sleep(50)
        main_obj.gmail_page.fill_and_send_mail_using_selenium()
        main_obj.close_web()
        main_obj.log.info("--- script in this web browser finished ---")
        main_obj.close_logger()


def setup():
    try:
        os.remove("log_file.log")
    except Exception as e:
        print(f"Failed to restart log file. error: {e}")
        os.close()
    load_dotenv()


if __name__ == '__main__':
    main()
