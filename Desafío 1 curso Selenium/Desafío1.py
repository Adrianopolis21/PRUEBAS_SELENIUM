import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com/text-box")
name = driver.find_element(By.ID,"userName")
name.send_keys("Adriano")
time.sleep(2)


mail = driver.find_element(By.ID,"userEmail")
mail.send_keys("adrianopolis@blablabla.com")
time.sleep(2)


current_adress = driver.find_element(By.ID,"currentAddress")
current_adress.send_keys("Taberna de Moe")
time.sleep(2)


permanent_adress = driver.find_element(By.ID,"permanentAddress")
permanent_adress.send_keys("Av. Siempre Viva 742")
time.sleep(2)

btn_send = driver.find_element(By.ID,"submit")
btn_send.click()
time.sleep(2)

acceso = driver.find_element(By.ID,"name")
if (acceso.text == "name"):
    print("DESAFÍO SUPERADO")