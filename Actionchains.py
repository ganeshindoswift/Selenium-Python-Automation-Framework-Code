from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

import time

driver=webdriver.Chrome(ChromeDriverManager().install())
# webdriver.get("https://www.spicejet.com")
# driver.get("https://paytm.com/")
# driver.get("https://www.irctc.co.in/nget/train-search")
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

time.sleep(3)
# if webdriver.find_element(By.XPATH, "//a[text()='Paytm for Consumer']").is_displayed(): ##paytm header navigation tab check
#     print("displayed")
# else:
#     print("not visible")
driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click() ##irctc.co.in  Alert OK button code.
# # btn=driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")

time.sleep(3)

alert=driver.switch_to.alert
alert.dismiss()
# alert.accept()
# # aler.accept()
time.sleep(3)
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
# action_chain=ActionChains(grand_link)
# action_chain.click()
time.sleep(3)
driver.close()
