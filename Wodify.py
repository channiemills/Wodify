__author__ = 'cmiller'


#from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By
from Wodify_Functions import login, element_wait, browser


login()

#open athlete dropdown
element_wait(By.ID, "W_Theme_UI_wt19_block_wtMainContent_wtAthleteDropDown_chosen").click()


#select athlete
browser.find_elements_by_class_name('active-result')[1].click()
#print athlete name
athlete_name = browser.find_element_by_xpath('//*[@id="W_Theme_UI_wt19_block_wtMainContent_wtAthleteDropDown_chosen"]/a/span')
print athlete_name.text
#iterate over this list somehow
#list = browser.find_elements_by_class_name('active-result')
#print list


#select type

type_dropdown = element_wait(By.ID, 'W_Theme_UI_wt19_block_wtMainContent_wtPCard_wtComponentTypeComboBox')
Select(type_dropdown).select_by_visible_text('Weightlifting')


#verify measure text boxes are present before setting component

element_wait(By.NAME, 'W_Theme_UI_wt19$block$wtMainContent$wtPCard$wt44')

#open component dropdown

element_wait(By.ID, 'W_Theme_UI_wt19_block_wtMainContent_wtPCard_wtComponentDropDown_chosen').click()

#select movement
#will need to iterate input over list of expected movements


element = element_wait(By.CSS_SELECTOR, '#W_Theme_UI_wt19_block_wtMainContent_wtPCard_wtComponentDropDown_chosen > a > span')
input = element_wait(By.CSS_SELECTOR, '#W_Theme_UI_wt19_block_wtMainContent_wtPCard_wtComponentDropDown_chosen > div > div > input[type="text"]')
input.send_keys('Back Squat\n')

print 'Back Squat'


#get 1 rep max
get_max = element_wait(By.XPATH, '//*[@id="W_Theme_UI_wt19_block_wtMainContent_wtPCard_W_Performance_UI_wt18_block_wtPRWrapper"]/table/tbody/tr[2]/td[1]')
max_value = get_max.text

print max_value


browser.quit()