from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains

# opciones del mavegador
options2=webdriver.EdgeOptions()
options2.add_argument('--disable-extensions')
options2.add_argument('--start-maximized')

driver=webdriver.Edge(executable_path="C:/Users/agosl/Downloads/edgedriver_win64/msedgedriver.exe", options=options2)

driver.get("https://shop.thonet-vander.com/")
time.sleep(3)
ActionChains(driver).send_keys(Keys.TAB * 4).perform()
time.sleep(2)
ActionChains(driver).send_keys(Keys.ENTER)
time.sleep(2)


driver.close()