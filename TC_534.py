#TC 534: MANTENIMINETO DE ELEMENTOS DEL CARRITO LUEGO DE CERRAR SESIÓN

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains

# opciones del mavegador
options2=webdriver.ChromeOptions()
options2.add_argument('--disable-extensions')
options2.add_argument('--start-maximized')

driver=webdriver.Chrome(executable_path="C:/Users/agosl/Downloads/chromedriver/chromedriver.exe", options=options2)

driver.get("https://shop.thonet-vander.com/")
time.sleep(3)
for i in range(2):
    login=driver.find_element(By.XPATH, '/html/body/header[1]/div[2]/div/div[3]/div/li[2]/a')
    login.click()
    time.sleep(1)
    mail=driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/form/input[1]')
    mail.click()
    time.sleep(1)
    mail.clear()
    time.sleep(1)
    mail.send_keys("cuentarandom@gmail.com")
    time.sleep(2)
    contra=driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/form/input[2]')
    contra.click()
    contra.send_keys("agostina11")
    time.sleep(1)
    contra.send_keys(Keys.ENTER)
    time.sleep(3)
    print("login successful")
    if(i==0):
        btn=driver.find_element(By.XPATH, '/html/body/div[7]/div/div[2]/div/div[1]/div[6]/li/div/div[1]/a/h2')
        btn.click()
        time.sleep(1.5)
        add=driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[2]/div[2]/div[1]/form/div/div[1]/div/button[2]')
        for i in range(4):
            add.click()
            time.sleep(1)
        cart=driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[2]/div[2]/div[1]/form/div/div[3]/button[2]').click()
        time.sleep(5)
        seguir=driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[3]/div[2]').click()
        time.sleep(1)
        print("Added to chart successfully")
        logo=driver.find_element(By.XPATH, '/html/body/header[1]/div[2]/div/div[1]/div').click()
        time.sleep(2)
        data=driver.find_element(By.XPATH, '/html/body/header[1]/div[2]/div/div[3]/div/li[1]/a[1]').click()
        time.sleep(1)
        cSesion=driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[1]/a').click()
        time.sleep(4)
    else:
        carrito=driver.find_element(By.XPATH, "/html/body/header[1]/div[2]/div/div[3]/div/li[2]/a").click()
        time.sleep(5)
        number=driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div/input")
       #no me toma esto
        if(number.get_property('value')==5 or number.get_dom_attribute("value")==5):
            print("test case pass")

        #<input type="number" class="js-cart-quantity-input cart-quantity-input count" id="cantidad_283258" value="21" 
        


driver.close()