
#TC ID 521: ACTUALIZACIÓN DE CARRITO EN TIEMPO REAL

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


# opciones del mavegador
options2=webdriver.EdgeOptions()
options2.add_argument('--disable-extensions')
options2.add_argument('--start-maximized')

driver=webdriver.Edge(executable_path="C:/Users/agosl/Downloads/edgedriver_win64/msedgedriver.exe", options=options2)

driver.get("https://shop.thonet-vander.com/")
time.sleep(2)
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

btn=driver.find_element(By.XPATH, '/html/body/div[7]/div/div[2]/div/div[1]/div[6]/li/div/div[1]/a/h2')
btn.click()
time.sleep(1.5)
add=driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[2]/div[2]/div[1]/form/div/div[1]/div/button[2]')
for i in range(4):
    add.click()
    time.sleep(1)
#no me deja clickear esto porque "otro elemento recibiría el click"
cart=driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[2]/div[2]/div[1]/form/div/div[3]/button[2]').click()
time.sleep(1)
seguir=driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[3]/div[2]/a').click()
time.sleep(1)
driver.close()