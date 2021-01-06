from selenium import webdriver
from pathlib import Path
import time

home = str(Path.home())

card_number = '____-___-___'
version_code = ''
secret_code = ''
first_name = ''
last_name = ''
dob_year = ''
dob_month = ''
dob_day = ''
sex = 'male'
postal_code = '___ ___'

chromedriver = home+"/Downloads/chromedriver"
driver = webdriver.Chrome(chromedriver)

driver.get('https://covid19results.ehealthontario.ca:4443/agree')

# Choose health card
driver.find_element_by_xpath(
    '//*[@id="step_1_div"]/div/div/div[1]/label/span[1]/span[3]').click()

# Handle animation delay
time.sleep(1)

# Confirm health card
driver.find_element_by_xpath('//*[@id="btn_step2_ohc_known"]').click()

# Agree to use information
driver.find_element_by_xpath(
    '//*[@id="step_agree_div"]/form/div/div[1]/div/label/span[1]/span[3]').click()

# Agree to use information
driver.find_element_by_xpath(
    '//*[@id="button_submit"]').click()

# Fill out form
driver.find_element_by_xpath('//*[@id="hcn"]').send_keys(card_number)
driver.find_element_by_xpath('//*[@id="vCode"]').send_keys(version_code)
driver.find_element_by_xpath('//*[@id="scn"]').send_keys(secret_code)
driver.find_element_by_xpath('//*[@id="fname"]').send_keys(first_name)
driver.find_element_by_xpath('//*[@id="lname"]').send_keys(last_name)
driver.find_element_by_xpath('//*[@id="dob-igc-yyyy"]').send_keys(dob_year)
driver.find_element_by_xpath('//*[@id="dob-igc-mm"]').send_keys(dob_month)
driver.find_element_by_xpath('//*[@id="dob-igc-dd"]').send_keys(dob_day)
if sex == 'male':
  button_sex = '//*[@id="login-form"]/div[6]/div/div[1]/div[1]/label/span[1]/span[3]'
elif sex == 'female':
  button_sex = '//*[@id="login-form"]/div[6]/div/div[1]/div[2]/label/span[1]/span[3]'
else:
  button_sex = '//*[@id="login-form"]/div[6]/div/div[1]/div[3]/label/span[1]/span[3]'


driver.find_element_by_xpath(button_sex).click()

driver.find_element_by_xpath('//*[@id="pCode"]').send_keys(postal_code)

driver.find_element_by_xpath('//*[@id="button_verify"]').click()
