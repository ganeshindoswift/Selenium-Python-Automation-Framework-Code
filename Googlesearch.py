from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time

driver= webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)

# driver.get("https://www.google.com/")
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
# #
# driver.find_element(By.NAME, "q").send_keys("Selenium locator")
# serch_list=driver.find_elements(By.XPATH, "//ul[1][@jsname='bw4e9b']/li")
#
# for i in serch_list:
#     element=i.text
#     print(element)

# assert driver.find_element(By.LINK_TEXT, "Why OrangeHRM").is_displayed()==True

# driver.find_element(By.LINK_TEXT, "Why OrangeHRM").click()

# if driver.find_element(By.LINK_TEXT, "Careers").is_displayed():
#     print("Carrers page link visible")
# else:
#     print("not visible")
#
count_listelemnt=driver.find_element(By.ID, "Form_getForm_Country")

select=Select(count_listelemnt)
# select.select_by_visible_text("India")
cont_elem=select.options
for ele in cont_elem:
    county=ele.text
    if county=="Guam":
        break
    print(county)

# Country_list=driver.find_elements(By.XPATH, "//select[@id='Form_getForm_Country']/option")
# print(len(Country_list))
#
#
# for country in Country_list:
#     contname=country.text
#     if contname=="Albania":
#         break
#     print(contname)
# #



#
# for elelist in len(serch_list):
#     elelist.text



time.sleep(4)
driver.close()