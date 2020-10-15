#Actualiza los precios de las tiendas
import threading
import pandas as pd
import os

import Scrapping_che as che
import Scrapping_comer_hbe as hbe
import Scrapping_lacomer as comer
import Scrapping_sor as sor


if __name__=='__main__':
    
    crearuta = r'csv' #ruta a crear carpeta donde guardar documentos csv
    if not os.path.exists(crearuta): os.makedirs(crearuta) # creacion de la carpeta
    #eliminar estas lineas en los scrapping de los otros py
    
    df = pd.DataFrame(list()) #Creando 5 documentos csv vacios para poner la info extraida de los comercios
    df.to_csv('csv/infofrutas.csv', encoding = 'utf8')
    df.to_csv('csv/infoverduras.csv', encoding = 'utf8')
    df.to_csv('csv/infolacteos.csv', encoding = 'utf8')
    df.to_csv('csv/infocarnes.csv', encoding = 'utf8')
    df.to_csv('csv/infoenlatados.csv', encoding = 'utf8')
    
    
    thread = threading.Thread(target = che.datosche) #Inicializando los hilos
    thread.start()
    
    thread2 = threading.Thread(target = hbe.extraerhbe) #Inicializar un hilo llamando a una funcion
    thread2.start()
    
    thread3 = threading.Thread(target = comer.extraerlacomer) #Inicializar un hilo llamando a una funcion
    thread3.start()
    
    thread4 = threading.Thread(target = sor.datossor) #Inicializar un hilo llamando a una funcion
    thread4.start()
    