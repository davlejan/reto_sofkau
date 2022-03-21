#librerias necesarias para el funcionamiento
from random import shuffle
from os import system
import json
import random

#Creando una clase "pregunta" la cual me pueda recibir los datos de mi base de datos
class pregunta:
      def  __init__(self,enunciado="",respuesta="",trampa1="",trampa2="",trampa3=""):
        
                self.enunciado = enunciado
                self.respuesta = respuesta
                self.trampa1 = trampa1
                self.trampa2 = trampa2
                self.trampa3 = trampa3