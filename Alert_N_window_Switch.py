from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
#************Rediffmail Login page automate*****************

driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
time.sleep(2)
# driver.find_element(By.ID, "login1").send_keys("ganeshindoswift")
# driver.find_element(By.ID, 'password').send_keys("ganesh@123")
# driver.find_element(By.NAME, "proceed").click()
# # alert=driver.switch_to.alert
# # alert.accept()

checkbox_status=driver.find_element(By.XPATH, "//input[@type='checkbox']").is_selected()
print(checkbox_status)
driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
#************Irctc search page automate*****************


time.sleep(5)


