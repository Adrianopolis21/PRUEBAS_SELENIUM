import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()


driver.get('https://institutoweb.com.ar/ejemplo1/')

lnk_contacto = driver.find_element(By.LINK_TEXT,"CONTACTO")


driver.switch_to.frame(0) #cambia la opcion de todos mis selectores al iframe seleccionado
btn_zoomin = driver.find_element(By.XPATH,'//*[@id=\"mapDiv\"]/div/div[3]/div[12]/div/div/div/button[1]')


btn_zoomout = driver.find_element(By.XPATH,'//*[@id=\"mapDiv\"]/div/div[3]/div[12]/div/div/div/button[2]')

driver.switch_to.default_content #cambia la opcion de todos mis selectores por defecto a la pagina principal


driver.close()

