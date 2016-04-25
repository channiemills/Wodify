__author__ = 'cmiller'


from selenium import webdriver
from selenium.webdriver.support.ui import Select
from Wodify_variables import username, password
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


browser = webdriver.Chrome()

browser.get('https://app.wodify.com/Performance/AthletePerformanceCardEntry.aspx')

username_field = browser.find_element_by_name('wt73$wtMainContent$wtUserNameInput')
username_field.send_keys(username)
password_field = browser.find_element_by_name('wt73$wtMainContent$wtPasswordInput')
password_field.send_keys(password)
#submit
browser.find_element_by_id('wt73_wtMainContent_wt59').click()

#time.sleep(2)


#writing a function to wait for elements

#element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "W_Theme_UI_wt19_block_wtMainContent_wtAthleteDropDown_chosen" )))

def element_wait(tag, element):
    global browser

    try:

        item = WebDriverWait(browser, 10).until(
            #EC.element_to_be_clickable((By.ID, "W_Theme_UI_wt19_block_wtMainContent_wtAthleteDropDown_chosen"))
            EC.element_to_be_clickable((tag, element))

        )

        return item

    except NoSuchElementException:
        browser.quit()
    #
    # finally:
    #     browser.quit()


element_wait(By.ID, "W_Theme_UI_wt19_block_wtMainContent_wtAthleteDropDown_chosen").click()

# print EC.presence_of_element_located((By.ID, 'W_Theme_UI_wt19_block_wtMainContent_wtAthleteDropDown_chosen'))
#
#
# try:
#     test = WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.ID, 'W_Theme_UI_wt19_block_wtMainContent_wtAthleteDropDown_chosen'))
#     )
#
# finally:
#     browser.quit()
#
# print test


# def helper_function(tag, element):
#     global browser
#     try:
#         test = WebDriverWait(browser, 10).until(
#             EC.presence_of_element_located((tag, element))
#         )
#
#     finally:
#         browser.quit()
#     return element


#
# helper_function(By.ID, 'W_Theme_UI_wt19_block_wtMainContent_wtAthleteDropDown_chosen')

#open athlete dropdown
#athlete_dropdown = helper_function(By.ID, 'W_Theme_UI_wt19_block_wtMainContent_wtAthleteDropDown_chosen')
#athlete_dropdown = browser.find_element_by_id('W_Theme_UI_wt19_block_wtMainContent_wtAthleteDropDown_chosen')

#browser.find_element_by_id(athlete_dropdown).click()
#athlete_dropdown.click()
#browser.find_element_by_id('W_Theme_UI_wt19_block_wtMainContent_wtAthleteDropDown_chosen').click()


time.sleep(2)
#select athlete
browser.find_elements_by_class_name('active-result')[1].click()
#print athlete name
athlete_name = browser.find_element_by_xpath('//*[@id="W_Theme_UI_wt19_block_wtMainContent_wtAthleteDropDown_chosen"]/a/span')
print athlete_name.text
#iterate over this list somehow
#list = browser.find_elements_by_class_name('active-result')
#print list

time.sleep(2)
#select type > not necessary
type_dropdown = Select(browser.find_element_by_id('W_Theme_UI_wt19_block_wtMainContent_wtPCard_wtComponentTypeComboBox'))
type_dropdown.select_by_visible_text('Weightlifting')

time.sleep(2)

#open component dropdown
browser.find_element_by_id('W_Theme_UI_wt19_block_wtMainContent_wtPCard_wtComponentDropDown_chosen').click()

#select movement
#will need to iterate input over list of expected movements
element = browser.find_element_by_css_selector('#W_Theme_UI_wt19_block_wtMainContent_wtPCard_wtComponentDropDown_chosen > a > span')
input = browser.find_element_by_css_selector('#W_Theme_UI_wt19_block_wtMainContent_wtPCard_wtComponentDropDown_chosen > div > div > input[type="text"]')
input.send_keys('Back Squat\n')

print 'Back Squat'


time.sleep(3)


#get 1 rep max
#get_max = browser.find_element_by_css_selector('#W_Theme_UI_wt19_block_wtMainContent_wtPCard_W_Performance_UI_wt18_block_wtPRWrapper > table > tbody > tr:nth-child(2) > td:nth-child(1)')
#get_max = browser.find_element_by_css_selector('//*[@id="W_Theme_UI_wt19_block_wtMainContent_wtPCard_W_Performance_UI_wt18_block_wtPRWrapper"]/table/tbody/tr[2]/td[1]')
get_max = browser.find_element_by_xpath('//*[@id="W_Theme_UI_wt19_block_wtMainContent_wtPCard_W_Performance_UI_wt18_block_wtPRWrapper"]/table/tbody/tr[2]/td[1]')
max_value = get_max.text

print max_value

time.sleep(2)

browser.quit()