__author__ = 'cmiller'


from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By
from Wodify_Functions import login, element_wait, browser, scores_wait

get_max = 0
max_value = 0

login()

### Open Athlete Dropdown ###
element_wait(By.ID, "W_Theme_UI_wt19_block_wtMainContent_wtAthleteDropDown_chosen").click()


### Select Athlete ###
browser.find_elements_by_class_name('active-result')[1].click()


### Print Athlete Name ###
athlete_name = browser.find_element_by_xpath('//*[@id="W_Theme_UI_wt19_block_wtMainContent_wtAthleteDropDown_chosen"]/a/span')
#print athlete_name.text
#iterate over this list somehow
#list = browser.find_elements_by_class_name('active-result')
#print list


### Set Type to Weightlifting ###

type_dropdown = element_wait(By.ID, 'W_Theme_UI_wt19_block_wtMainContent_wtPCard_wtComponentTypeComboBox')
Select(type_dropdown).select_by_visible_text('Weightlifting')


### Verify Measure Text Box Present Before Setting Component ###

element_wait(By.NAME, 'W_Theme_UI_wt19$block$wtMainContent$wtPCard$wt44')


### Select Component ###
#will need to iterate input over list of expected components

component_file = open("movements", "r")
components = [line.rstrip('\n') for line in component_file]


def set_components():
    global get_max, max_value, athlete_name

    scores = []
    for i in components:
        element_wait(By.ID, 'W_Theme_UI_wt19_block_wtMainContent_wtPCard_wtComponentDropDown_chosen').click()
        input = element_wait(By.CSS_SELECTOR, '#W_Theme_UI_wt19_block_wtMainContent_wtPCard_wtComponentDropDown_chosen > div > div > input[type="text"]')
        input.send_keys(i + '\n')
        #print i
  ### Get 1 Rep Max ###
        if scores_wait(By.CLASS_NAME, 'highcharts-title', (i + ' History over Time')) == None:
            #print 'N/A'
            scores.append('N/A')
        else:
            scores_wait(By.CLASS_NAME, 'highcharts-title', (i + ' History over Time'))
            get_max = element_wait(By.XPATH, '//*[@id="W_Theme_UI_wt19_block_wtMainContent_wtPCard_W_Performance_UI_wt18_block_wtPRWrapper"]/table/tbody/tr[2]/td[1]')
            max_value = get_max.text.strip(' lbs')
            #print max_value
            scores.append(max_value)
            performance = dict(zip(components, scores))
            performance['Athlete'] = athlete_name.text
    print performance

#for data storage, i could write the maxes to a list then add athlete name to components and that array then create a dict?


set_components()

browser.quit()