# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 23:59:01 2020

@author: Carlos Venegas
"""
#segmento de código para hacer una pausa en la ejecución

from time import sleep
from random import randint
for esp in range(0,5):
    print('Blah')
   # sleep(randint(1,4))

#segmento con el cual se hacer peticiones cada cierta
#cantidad de tiempo
from time import time
from IPython.core.display import clear_output
requests = 0
start_time = time()
#print('start_time')
#print(start_time)
for i in range(5):
    #Una peticion debe ir aqui
    requests += 1
    sleep(randint(1,3))
    current_time = time()
    elapsed_time = current_time - start_time
   #print('elapsed_time')
   # print(elapsed_time)
    print('Request: {}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
    #clear_output(wait = True)
    
from warnings import warn
warn("Warning Simulation")