def obtener_selectores():
    #Escribir los selectores del test case
    #Estructura del tipo diccionario de python
    pantalla = {
        "menu":{
            "contactenos" :"CONTACT"
        },
        "iframe":{
            "zoom-in" :  "//*[@id=\'mapDiv\']/div/div[3]/div[12]/div/div/div/button[1]",
            "zoom-out" : "//*[@id=\'mapDiv\']/div/div[3]/div[12]/div/div/div/button[2]"


        }
    }


    # Devolver datos
    return pantalla
