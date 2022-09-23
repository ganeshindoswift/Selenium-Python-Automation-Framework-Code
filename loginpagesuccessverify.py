from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
#
#
import time

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys('Admin')
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys('admin123')
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# if driver.find_element(By.XPATH, "//h6[text()='PIM']").is_displayed():
#     print("success")
# else:
#     print("not suceess")


# #
# assert driver.find_element(By.CSS_SELECTOR, 'h6.oxd-text.oxd-text--h6.oxd-topbar-header-breadcrumb-module').is_displayed()==True
# assert driver.find_element(By.XPATH, "//a[@role='menuitem' and @href='/web/index.php/auth/logout']").is_displayed()==True

driver.find_element(By.XPATH, "//p[text()='Paul Collings']").click()
# driver.find_element(By.XPATH, " //a[text()='Logout']").click()
assert driver.find_element(By.XPATH, " //a[text()='Logout']").is_displayed()==True

time.sleep(5)

driver.close()
