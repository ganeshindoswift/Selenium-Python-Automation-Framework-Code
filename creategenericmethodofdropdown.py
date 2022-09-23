import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('https://www.facebook.com/')
driver.find_element(By.XPATH, "//*[text()='Create New Account']").click()


def select_DOB(refrencelocator, value):
    day_select=Select(refrencelocator)
    day_select.select_by_visible_text(value)
    month_select=Select(refrencelocator)
    month_select.select_by_visible_text(value)
    year_select=Select(refrencelocator)
    year_select.select_by_visible_text(value)

day_list=driver.find_element(By.ID, "day")
month_list=driver.find_element(By.ID, "month")
year_list=driver.find_element(By.ID, "year")

select_DOB(day_list, "3")
select_DOB(month_list, 'Jan')
select_DOB(year_list, "2020")

time.sleep(3)