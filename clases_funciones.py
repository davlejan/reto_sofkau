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

#Creo una funcion la cual dependiendo de la ronda (nivel) en que este me devuelve la categoria adecuada

def nivel_categoria(nivel):
                  if nivel == 0:
                              return 'deporte'
                  if nivel == 1:
                              return 'cultura general'
                  if nivel == 2:
                              return 'geografia'
                  if nivel == 3:
                              return 'historia'
                  if nivel == 4:
                              return 'matematicas'  

#creo una funcion que me permita llevar la puntuacion dependiendo de la ronda (doble puntos  cada ronda)

def puntuacion(ronda_actual,puntuacion_actual=0):
                  if ronda_actual == 0:
                              return puntuacion_actual + 1
                  if ronda_actual == 1:
                              return puntuacion_actual + 2
                  if ronda_actual == 2:
                              return puntuacion_actual + 4
                  if ronda_actual == 3:
                              return puntuacion_actual + 8
                  if ronda_actual == 4:
                              return puntuacion_actual + 16     

#Creo una funcion para pedir el nombre del jugador (alivianar un poco la funcion ronda)

def pedir_nombre_usuario():
            system('clear')
            print('Por favor digita tu nombre de usuario')
            return input()

#Creo la clase datos_de personaje para manejar los datos del jugador y llevarlos a la base de datos historica

class datos_personaje:
            def __init__(self,nombre_personaje="",puntuacion=0):
                        self.nombre_personaje = nombre_personaje
                        self.puntuacion = puntuacion

            #Creo metodo para mantener el puntaje actualizado      
            def incrementar_puntuacion(self,nueva_puntuacion):
                        self.puntuacion = self.puntuacion + nueva_puntuacion

            #Creo una funcion para guardar en el historial el puntaje del jugador (en los casos requeridos)
            def guardar_historial(self,url):
                        #abro el archivo y lo trato para poder manipularlo facilmente con python
                        abrir_archivo = open(url)
                        leer_archivo = abrir_archivo.read()
                        historial_js = json.loads(leer_archivo)
                        #Agrego a la lista los datos del usuario 
                        historial_js.append(
                        {
                              "ranking": len(historial_js)+1,
                              "nombre_usuario": self.nombre_personaje,
                              "puntuacion": self.puntuacion

                        }
                        )
                        # con un algoritmo de ordenamiento burbuja pongo en el lugar que corresponde segun la puntuacion
                        n = len(historial_js)
                        for i in range(n):
                              for j in range(0,n-i-1):
                                    if historial_js[j]["puntuacion"] < historial_js[j+1]["puntuacion"]:
                                          historial_js[j],historial_js[j+1] = historial_js[j+1],historial_js[j]
                                          historial_js[j]["ranking"], historial_js[j+1]["ranking"] = historial_js[j+1]["ranking"],historial_js[j ]["ranking"]

                        #abro nuevamente el archivo para escribir los nuevos datos (con los nuevos ya agregados y organizados)
                        print(historial_js)
                        with open(url,'w') as j:
                              json.dump(historial_js,j)


#Creo mi funcion ronda la cual se ecarga de todo lo referente a las diferentes etapas del juego

def ronda(nombre_usuario):
            jugador = datos_personaje(nombre_usuario)
            #Creo ciclo for que se encargara de las 5 rondas del juego
            for i in range(5):
                        system("clear")
                        print(nivel_categoria(i))
                        #desde mi clase pregunta llamo una pregunta acorde al nivel solicitado enviando Url y categoria
                        pregunta.cargar_pregunta('preguntas.json',nivel_categoria(i))
                        #con mi funcion dar_pregunta le entrengo al usuario la pregunta y las posibles respuestas
                        #adicional evalua si es correcta 
                        acierto=pregunta.dar_pregunta()
                        if acierto == True:
                                    #al acertar la prgunta incremento la puntuacion del jugador
                                    jugador.incrementar_puntuacion(puntuacion(i,jugador.puntuacion))  
                                    system("clear")
                                    #Pregunto al usuario si desea continuar con el juego 
                                    while True:
                                                #condicional añadido para terminar el juego al responder la ultima pregunta
                                                if i == 4:
                                                      system("clear")
                                                      #guarda el historial del jugador al ganar el juego
                                                      jugador.guardar_historial('historial.json')
                                                      print('Ganaste! (oprime enter para continuar)')
                                                      input()
                                                      #me regresa al menu principal
                                                      pagina_principal()
                                                #parte donde evalua si el usuario desea continuar
                                                print(f'respuesta correcta,¿Desea continuar? \n {nombre_usuario} tu puntuacion actual es {jugador.puntuacion} \n Y para continuar \n N para salvar puntuacion')
                                                respuesta_continuar = input().upper()
                                                if respuesta_continuar == 'Y':
                                                            break
                                                if respuesta_continuar == 'N':
                                                            #si el usuario no desea continuar guarda los datos en el historico
                                                            jugador.guardar_historial('historial.json')
                                                            #me regresa al menu principal
                                                            pagina_principal()

                                                else:
                                                            system("clear")
                                                            print('ingrese un dato valido')
                        #si el usuario no responde de manera acertada lo devuelve al menu principal y no guarda el historial                                  
                        if acierto == False:
                                    system("clear")
                                    print('Respondio incorrectamente, sus puntos ganados no se guardaran en el historial (presiona enter para continuar)')
                                    input()
                                    pagina_principal()

#Creo la funcion que gestiona el menu del juego 

def pagina_principal():
            system("clear")
            
            while True:
                        print('Bienvenido al juego Preguntas y respuestas \n Presione 1 para comenzar un juego nuevo \n Presione 2 para ver historial de puntuacion \n presione 3 para salir')
                        seleccion_usuario = input()
                        #opcion para inicializar el juego
                        if seleccion_usuario == '1':
                                    ronda(pedir_nombre_usuario())
                        #lee el historial y lo imprime en consola
                        if seleccion_usuario == '2':
                                    system("clear")
                                    abrir_archivo = open('historial.json')
                                    leer_archivo = abrir_archivo.read()
                                    historial_js = json.loads(leer_archivo)
                                    print(len(historial_js))
                                    for i in range(len(historial_js)):
                                                print(f'Ranking:{historial_js[i]["ranking"]} jugador:{historial_js[i]["nombre_usuario"]} Puntuacion:{historial_js[i]["puntuacion"]} ')
                                    print('Presione Enter para Salir')
                                    input()
                                    pagina_principal()
                        #forza al sistema a salir
                        if seleccion_usuario == '3':
                                    quit()
                        else:
                                    system("clear")
                                    print('seleccione una de las opciones correctamente')

if __name__ == "__main__":

    pregunta = pregunta()
    pagina_principal()