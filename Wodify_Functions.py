__author__ = 'cmiller'

from selenium import webdriver
from Wodify_variables import username, password
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
#from Wodify import browser


browser = webdriver.Chrome()


def login():
    global browser
    browser.get('https://app.wodify.com/Performance/AthletePerformanceCardEntry.aspx')
    username_field = browser.find_element_by_name('wt73$wtMainContent$wtUserNameInput')
    username_field.send_keys(username)
    password_field = browser.find_element_by_name('wt73$wtMainContent$wtPasswordInput')
    password_field.send_keys(password)
    browser.find_element_by_id('wt73_wtMainContent_wt59').click()


def element_wait(tag, element):
    global browser

    try:

        item = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((tag, element))
        )

        return item

    except TimeoutException:
        browser.quit()