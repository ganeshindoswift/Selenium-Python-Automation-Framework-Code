from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager


import time
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
time.sleep(2)
# driver.find_element(By.XPATH, "//input[@name='subdomain']").send_keys("Vikrama")
# driver.find_element(By.XPATH, "//input[@name='Name']").send_keys("ganesh Prasad Shah")
# driver.find_element(By.XPATH, "//input[@type='text']").send_keys("ganeshindoswift@gmail.com")
# driver.find_element(By.XPATH, "//input[@name='Contact']").send_keys("9795002134")
# # driver.find_element(By.ID, "input#Form_getForm_Name.text").send_keys("Ganesh Prasad Shah")
# # driver.find_element(By.ID, "#Form_getForm_Email").send_keys("ganeshindoswiftt@rediffmail.com")
# # driver.find_element(By.ID, "$Form_getForm_Contact").send_keys("7400349193")
# # country=driver.find_element(By.ID, "#Form_getForm_Country")
# countylist=driver.find_element(By.XPATH, "//select[@name='Country']")
# select=Select(countylist)
# select.select_by_visible_text("India")

chek=driver.find_element(By.XPATH, "//span[@role='checkbox']").click()
print(chek)

# driver.find_element(By.ID, "recaptcha-anchor").click()

time.sleep(2)

