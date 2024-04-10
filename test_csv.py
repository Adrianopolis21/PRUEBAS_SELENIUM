import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://institutoweb.com.ar/test/login.html")

with open("datos.csv") as datos: #apertura de la conexión al archivo csv con Python
    todos_datos = csv.reader(datos) #todos los renglones del archivo
    for renglon in todos_datos: #bucle de leer un renglon a la vez
        usuario,clave,mail = renglon #guardo en 3 variables por renglon
        txt_usuario = driver.find_element(By.ID,"tuusuario")
        txt_usuario.send_keys(usuario)

        txt_clave = driver.find_element(By.ID,"tuclave")
        txt_clave.send_keys(clave)

        txt_mail = driver.find_element(By.ID,"tumail")
        txt_mail.send_keys(mail)

        btn_ingresar = driver.find_element(By.CSS_SELECTOR,"body > form > button:nth-child(8)")
        btn_ingresar.click()
        time.sleep(4)

        btn_cerrar = driver.find_element(By.ID,"#volver")
        btn_cerrar.click()