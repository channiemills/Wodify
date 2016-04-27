__author__ = 'cmiller'

from selenium import webdriver
from Wodify_variables import username, password
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


browser = webdriver.Chrome()
no_data = 'Sorry, no performance history.'


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


def scores_wait(tag, element, component):
    global browser

    try:

        item = WebDriverWait(browser, 3).until(
            EC.text_to_be_present_in_element((tag, element), component)
        )

        return item

    except TimeoutException:
        if browser.find_element_by_id('W_Theme_UI_wt19_block_wtMainContent_wtPCard_W_Performance_UI_wt18_block_wtPerformanceResultsWrapper').text == no_data:
            return None
