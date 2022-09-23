import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('https://www.facebook.com/')
# driver.find_element(By.ID, "#u_0_0_C3").click()
driver.find_element(By.XPATH,"//*[text()='Create New Account']").click()
time.sleep(4)
driver.close()