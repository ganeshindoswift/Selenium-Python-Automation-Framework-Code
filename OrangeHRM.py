from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager


import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
driver.find_element()