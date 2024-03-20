import os

from Utilities.BaseClass import BaseClass
from dotenv import load_dotenv


def main():
    for index in range(3):
        setup()
        main_obj = BaseClass(index)
        main_obj.landing_page.change_language()
        # main_obj.landing_page.exit_script()
        main_obj.landing_page.choose_city()
        main_obj.landing_page.scrap_content()
        main_obj.landing_page.open_new_tab()
        main_obj.gmail_page.open_gmail()
        main_obj.gmail_page.log_in_gmail()
        main_obj.gmail_page.create_new_mail()
        main_obj.gmail_page.fill_and_send_mail_using_selenium()
        main_obj.close_web()
        main_obj.close_logger()
        main_obj.landing_page.exit_script()



def setup():
    try:
        os.remove("log_file.log")
    except:
        print("Failed to restart log file")
        os.close()
    load_dotenv()


if __name__ == '__main__':
    main()
