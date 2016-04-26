__author__ = 'cmiller'


from selenium import webdriver
from selenium.webdriver.support.ui import Select
from Wodify_variables import username, password
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException


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
def element_wait(tag, element):
    global browser

    try:

        item = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((tag, element))
        )

        return item

    except TimeoutException:
        browser.quit()


#open athlete dropdown
element_wait(By.ID, "W_Theme_UI_wt19_block_wtMainContent_wtAthleteDropDown_chosen").click()


#former open athlete dropdown
#athlete_dropdown = browser.find_element_by_id('W_Theme_UI_wt19_block_wtMainContent_wtAthleteDropDown_chosen')
#athlete_dropdown.click()


#time.sleep(2)
#select athlete
browser.find_elements_by_class_name('active-result')[1].click()
#print athlete name
athlete_name = browser.find_element_by_xpath('//*[@id="W_Theme_UI_wt19_block_wtMainContent_wtAthleteDropDown_chosen"]/a/span')
print athlete_name.text
#iterate over this list somehow
#list = browser.find_elements_by_class_name('active-result')
#print list

#time.sleep(2)
#select type

type_dropdown = element_wait(By.ID, 'W_Theme_UI_wt19_block_wtMainContent_wtPCard_wtComponentTypeComboBox')
Select(type_dropdown).select_by_visible_text('Weightlifting')

# type_dropdown = Select(browser.find_element_by_id('W_Theme_UI_wt19_block_wtMainContent_wtPCard_wtComponentTypeComboBox'))
# type_dropdown.select_by_visible_text('Weightlifting')

#time.sleep(2)

# the problem is that the element is clickable but there is nothing in it yet so it closes

# def set_component():
# # need a function to retry until components are fully loaded
#     for attempt in range(10):
#         try:
#             #open component dropdown
#             element_wait(By.ID, 'W_Theme_UI_wt19_block_wtMainContent_wtPCard_wtComponentDropDown_chosen').click()
#             element = element_wait(By.CSS_SELECTOR, '#W_Theme_UI_wt19_block_wtMainContent_wtPCard_wtComponentDropDown_chosen > a > span')
#             #element = browser.find_element_by_css_selector('#W_Theme_UI_wt19_block_wtMainContent_wtPCard_wtComponentDropDown_chosen > a > span')
#             input = element_wait(By.CSS_SELECTOR, '#W_Theme_UI_wt19_block_wtMainContent_wtPCard_wtComponentDropDown_chosen > div > div > input[type="text"]')
#             #input = browser.find_element_by_css_selector('#W_Theme_UI_wt19_block_wtMainContent_wtPCard_wtComponentDropDown_chosen > div > div > input[type="text"]')
#             input.send_keys('Back Squat\n')
#             break
#         except AttributeError:
#             pass
#         # else:
#         #     break
#
#
# set_component()

#verify measure text boxes are present before setting component

element_wait(By.NAME, 'W_Theme_UI_wt19$block$wtMainContent$wtPCard$wt44')

#open component dropdown


element_wait(By.ID, 'W_Theme_UI_wt19_block_wtMainContent_wtPCard_wtComponentDropDown_chosen').click()
#browser.find_element_by_id('W_Theme_UI_wt19_block_wtMainContent_wtPCard_wtComponentDropDown_chosen').click()

#time.sleep(5)
#print 'Did you wait?'


#select movement
#will need to iterate input over list of expected movements


element = element_wait(By.CSS_SELECTOR, '#W_Theme_UI_wt19_block_wtMainContent_wtPCard_wtComponentDropDown_chosen > a > span')
# #element = browser.find_element_by_css_selector('#W_Theme_UI_wt19_block_wtMainContent_wtPCard_wtComponentDropDown_chosen > a > span')
input = element_wait(By.CSS_SELECTOR, '#W_Theme_UI_wt19_block_wtMainContent_wtPCard_wtComponentDropDown_chosen > div > div > input[type="text"]')
# #input = browser.find_element_by_css_selector('#W_Theme_UI_wt19_block_wtMainContent_wtPCard_wtComponentDropDown_chosen > div > div > input[type="text"]')
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