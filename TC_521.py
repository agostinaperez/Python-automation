
#TC ID 521: ACTUALIZACIÓN DE CARRITO EN TIEMPO REAL

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
mail.send_keys("cuentarandom@gmail.com")
time.sleep(2)
contra=driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/form/input[2]')
contra.click()
contra.send_keys("agostina11")
time.sleep(1)
contra.send_keys(Keys.ENTER)
time.sleep(3)

producto1=driver.find_element(By.XPATH, '/html/body/div[7]/div/div[2]/div/div[1]/div[7]/li/div/div[1]/div/a[2]')
#Esta parte se ve media feita
driver.execute_script("arguments[0].scrollIntoView(true);",producto1)
time.sleep(2)
producto1.click()
time.sleep(2)
addButton=driver.find_element(By.XPATH, '/html/body/div[7]/div/div[2]/div/div[1]/div[7]/li/div/div[1]/div/a[2]')
addButton.click()
time.sleep(1)
cant=driver.find_element(By.XPATH, '/html/body/div[12]/div[2]/div[4]/div/form/div[4]/div/button[2]')
for i in range(2):
    cant.click()
    time.sleep(1)

addButton=driver.find_element(By.XPATH, '/html/body/div[12]/div[2]/div[4]/div/form/div[4]/button')
addButton.click()
time.sleep(2)

driver.close()