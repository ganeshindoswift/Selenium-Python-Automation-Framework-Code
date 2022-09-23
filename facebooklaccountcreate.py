import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('https://www.facebook.com/')
# driver.find_element(By.CSS_SELECTOR, '*#email').send_keys('ganesh_indoswift@yahoo.com')
# driver.find_element(By.CSS_SELECTOR, 'input.inputtext#pass').send_keys('markiv')
# driver.find_element(By.NAME, 'login').click()

# driver.find_element(By.ID, "#u_0_0_C3").click()
driver.find_element(By.XPATH,"//*[text()='Create New Account']").click()
driver.find_element(By.NAME, 'firstname').send_keys('Ganesh')
driver.find_element(By.NAME, 'lastname').send_keys('Shah')
driver.find_element(By.NAME, 'reg_email__').send_keys('ganeshindoswift@gmail.com')
driver.find_element(By.NAME, "reg_email_confirmation__").send_keys('ganeshindoswift@gmail.com')
driver.find_element(By.NAME, 'reg_passwd__').send_keys('ganesh123')

elem_day=driver.find_element(By.ID, "day")
select=Select(elem_day)
day_list=select.options

for d in day_list:
    print(d)


# day.select_by_visible_text('2')
# day=Select(driver.find_element(By.CSS_SELECTOR, '#day'))
# day.select_by_visible_text("10")
# month=Select(driver.find_element(By.CSS_SELECTOR,'#month'))
# month.select_by_visible_text('Feb')
# year=Select(driver.find_element(By.CSS_SELECTOR, '#year'))
# year.select_by_visible_text('2020')
# # #
# driver.find_element(By.XPATH, "//label[text()='Female']").click()
# driver.find_element(By.XPATH, "//button[text()='Sign Up' and @name='websubmit']").click()


time.sleep(3)
driver.close()