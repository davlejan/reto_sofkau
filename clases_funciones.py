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

#creo un metodo dentro de la clase que me permite desde la url de mi base de datos cargar 
#los datos de las preguntas
      def cargar_pregunta(self,url,categoria):
            #desde la url leo la base datos
                  bd_preguntas = open(url)
                  todas_preguntas = bd_preguntas.read()
            #convierto el archivo en un diccionario que pueda interpretar python      
                  preguntas_js = json.loads(todas_preguntas)
            #creo una nueva lista filtrada por la categoria que corresponde al nivel requerido      
                  nueva_lista = [x for x in preguntas_js if x["categoria"] == categoria]
            #de manera aleatoria entre las opciones de la categoria escojo una de las preguntas      
                  aleatorio = random.randint(0, len(nueva_lista)-1)
                  pregunta_aleatoria = nueva_lista[aleatorio]
            #llevo estos nuevos datos sacados de mi base de datos a las variables de mi clase pregunta      
                  self.enunciado = pregunta_aleatoria["pregunta"]
                  self.respuesta = pregunta_aleatoria["respuesta"]
                  self.trampa1 = pregunta_aleatoria["trampa1"]
                  self.trampa2 = pregunta_aleatoria["trampa2"]
                  self.trampa3 = pregunta_aleatoria["trampa3"]                


 #realizo un metodo para la clase pregunta el cual organiza las respuestas de forma aletoria
 # adicionalmente imprime el enunciado y las preguntas y evalua si la respuesta es correcta
 # devolviendome True si es correcta False si no lo es y entrando en un bucle si la letra no es valida            
      
      def dar_pregunta(self):
                  #llevo las respuestas a un arreglo el cual pongo de forma aleatoria las respuestas
                  #con la funcion shuffle
                   respuestas = [self.respuesta,self.trampa1,self.trampa2,self.trampa3]
                   shuffle(respuestas)
                  #entro en un bucle while para obtener una respuesta valida 
                   while True:
                              #imprimo el enunciado y las respuestas de forma aleatoria
                              print( self.enunciado)
                              print(f' A {respuestas[0]} \n B {respuestas[1]} \n C {respuestas[2]} \n D {respuestas[3]} \n Digite su respuesta')
                              respuesta_usuario = input().upper()
            
                              #Evaluo la respuesta del usuario, si es correcta o no
                              if respuesta_usuario == 'A':
                                          if  respuestas[0] == self.respuesta:
                                                      return True
                                                      break
                                          else: 
                                                return False
                                                break
                              if respuesta_usuario == 'B':
                                          if  respuestas[1] == self.respuesta:
                                                return True
                                                break
                                          else: 
                                                return False
                                                break
                              if respuesta_usuario == 'C':
                                          if  respuestas[2] == self.respuesta:
                                                return True
                                                break
                                          else: 
                                                return False
                                                break
                              if respuesta_usuario == 'D':
                                          if  respuestas[3] == self.respuesta:
                                                return True
                                                break
                                          else: 
                                                return False
                                                break
                              #en caso de no se run dato valido pido nuevamente la respuesta            
                              else: 
                                          system("clear")
                                          print('Ingrese un dato valido')           