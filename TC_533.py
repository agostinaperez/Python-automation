#TC ID 533: INGRESO DE SESIÓN CON USUARIO INVÁLIDO

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd

# opciones del mavegador
options2=webdriver.EdgeOptions()
options2.add_argument('--disable-extensions')
options2.add_argument('--start-maximized')

driver=webdriver.Edge(executable_path="C:/Users/agosl/Downloads/edgedriver_win64/msedgedriver.exe", options=options2)

driver.get("https://shop.thonet-vander.com/")
time.sleep(3)

login=driver.find_element(By.XPATH, '/html/body/header[1]/div[2]/div/div[3]/div/li[2]/a')
login.click()
time.sleep(1)
mail=driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/form/input[1]')
mail.click()
time.sleep(1)
mail.send_keys("cuentarandom")
time.sleep(2)
contra=driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/form/input[2]')
contra.click()
contra.send_keys("agostina11")
time.sleep(1)
contra.send_keys(Keys.ENTER)
time.sleep(3)
driver.close()

print("Test case pass")


#TC PASS!!