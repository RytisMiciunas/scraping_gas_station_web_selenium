from selenium.webdriver.common.by import By

FIND_ANYTHING = (By.XPATH, "//body")
LT_LANGUAGE_BUTTON = (By.LINK_TEXT, "Lietuva")
CITIES_DROPBOX = (By.ID, "cities")
VILNIUS_OPTION_IN_DROPBOX = (By.XPATH, "//option[@value='Vilnius']")
SELECT_DYZEL = (By.XPATH, "//th[2]")
ALL_DYZEL = (By.XPATH, "//tbody/tr/td[2]")
YAHOO_LOGIN_MAIL_INPUT = (By.ID, "login-username")
YAHOO_SUBMIT_MAIL_BUTTON = (By.ID, "login-signin")
GMAIL_LOGIN_MAIL_INPUT = (By.ID, "identifierId")
GMAIL_SUBMIT_MAIL_BUTTON = (By.XPATH, "//span[contains(text(), 'Next')]")
GMAIL_LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@name='Passwd']")
GMAIL_CREATE_NEW_LETTER_BUTTON = (By.XPATH, "//div[contains(text(), 'Compose')]")
GMAIL_MAIL_TO_RECIEVER = (By.XPATH, "//input[@aria-label='To recipients']")
GMAIL_MAIL_RECIEVER = (By.XPATH, "//input[@aria-label='Recipients']")
GMAIL_MAIL_SUBJECT = (By.XPATH, "//input[@name='subjectbox']")
GMAIL_MAIL_CONTENT = (By.XPATH, "//div[@role='textbox']")
GMAIL_MAIL_SEND_BUTTON = (By.XPATH, "//div[contains(@role, 'button') and text() = 'Send']")
GMAIL_SUCCESS_POPUP = (By.XPATH, "//span[contains(text(), 'Message sent')]")







