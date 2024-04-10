import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()


driver.get('https://institutoweb.com.ar/test/login.html')
try: # probá este código
    with open('datos.json') as datos: # apertura de la conexión al archivo
        todos_los_datos = json.load(datos)  #todos los renglones del archivo
        for renglon in todos_los_datos: #bucle de leer de a un renglon a la vez
            # guardo en tres variables
            mi_usuario = renglon['usuario']
            su_clave = renglon['clave']
            el_mail = renglon['email']


            txt_usuario = driver.find_element(By.ID,"tuusuario")
            txt_usuario.send_keys(mi_usuario)


            txt_clave = driver.find_element(By.ID,"tuclave")
            txt_clave.send_keys(su_clave)


            txt_email = driver.find_element(By.ID,"tumail")
            txt_email.send_keys(el_mail)


            time.sleep(5)


            btn_ingresar = driver.find_element(By.CSS_SELECTOR,"body > form > button:nth-child(8)")
            btn_ingresar.click()


            lnk_volver = driver.find_element(By.ID,"volver")
            time.sleep(3)
            lnk_volver.click()
            time.sleep(3)
except FileNotFoundError : #Error clasificado como
            print("No se encontró el archivo")
            driver.close()            
except Exception as detalle: # si ocurre un error no clasificado
            print("ocurrió un error que no sé que es")
            driver.close()