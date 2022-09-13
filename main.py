print('Bienvenido primer jugador, la temática consiste acerca de Marvel comics. \n')
import random
import time

BLACK = '\033[30m'
RED ='\033[31m'
GREEN ='\033[32m'
YELLOW ='\033[33m'
BLUE ='\033[34m'
MAGENTA ='\033[35m'
CYAN ='\033[36m'
WHITE ='\033[37m'
RESET ='\033[39m'
iniciar_trivia = True
intentos = 0
puntaje = random.randint( 0, 10 )
nombre = input('Ingresa tu nombre:')


print('Hola', nombre, 'deberas escribir la letra de la respuesta que te parezca correcta, presionando enter. \n')
print('Te deseo suerte acumulando el mayor puntaje posible. \n')
print(CYAN+'¡QUE COMIENCE EL JUEGO! \n'+ RESET)


print('\n 1) ¿Quien fue nombrado el primer vengador? \n')
print('a) Hulk')
print('b) Iron Man')
print('c) Capitan America')
print('d) Ojo de halcon \n')

respuesta_1 = input ('\n Tu respuesta: ') 
for numero_carga in range(3, -1, -1):
    print(f'\r{numero_carga}', end = '')
    time.sleep(1)  
if respuesta_1 == 'c':
   print(GREEN+'¡MUY BIEN!'+RESET)
   puntaje += 10
else:
   print(RED+'¡INCORRECTO!\n'+RESET)
while respuesta_1 not in ('a', 'b', 'c', 'd'):
      respuesta_1 =input(RED+'Debes responder a, b, c, o d. Ingresa nuevamente tu respuesta: '+RESET)


  

print('\n 2) ¿Cual es el nombre verdadero de Sunspot? \n')
print('a) Roberto DaCosta')
print('b) Anthony Edward Stark')
print('c) James Buchanan Barnes')
print('d) Steven Grant Rogers')

respuesta_2 = input ('\n Tu respuesta: ')
while respuesta_2 not in ('a', 'b', 'c', 'd'):
      respuesta_2 = input('Debes responder a, b, c, o d. Ingresa nuevamente tu respuesta: ')
for numero_carga in range(3, -1, -1):
    print(f'\r{numero_carga}', end = '')
    time.sleep(1)  
if respuesta_2 == 'b':
 print(RED+'INCORRECTO', nombre, 'su alias de Anthony Edward Stark es Iron man'+RESET)
 puntaje = puntaje - 1
elif respuesta_2 == 'c':
 print(RED+'INCORRECTO', nombre, 'su alias de James Buchanan Barnes es El soldado del invierno'+RESET) 
 puntaje = puntaje - 1
elif respuesta_2 == 'd':
 print(RED+'INCORRECTO', nombre, 'su alias de Steven Grant Rogers es Capitan america'+RESET) 
 puntaje = puntaje - 1
else:
 puntaje += 10 
 print(GREEN+'¡MUY BIEN', nombre, '!'+RESET)


print('\n 3) ¿Quien es un velocista? \n')
print('a) Super sabre')
print('b) Cannonball')
print('c) Havok')
print('d) Warpath')

respuesta_3 = input ('\n Tu respuesta: ')
while respuesta_3 not in ('a', 'b', 'c', 'd'):
      respuesta_3 = input('Debes responder a, b, c, o d. Ingresa nuevamente tu respuesta: ')
for numero_carga in range(3, -1, -1):
    print(f'\r{numero_carga}', end = '')
    time.sleep(1)  
if respuesta_3 == 'b':
 print(RED+'INCORRECTO', nombre, 'Cannonball es un hombre cohete'+RESET) 
 puntaje = puntaje - 1
elif respuesta_3 == 'c':
 print(RED+'INCORRECTO', nombre, 'Havok emana energia de su cuerpo'+RESET) 
 puntaje = puntaje - 1
elif respuesta_3 == 'd':
 print(RED+'INCORRECTO', nombre, 'Warpath tiene fuerza sobre humana'+RESET) 
 puntaje = puntaje - 1
else:
 puntaje += 10 
 print(GREEN+'¡MUY BIEN', nombre, '!'+RESET)


print('\n 4) ¿Que superheroe es un mutante? \n')
print('a) Spiderman')
print('b) Night thrasher')
print('c) Sunfire')
print('d) Crystal')

respuesta_4 = input ('\n Tu respuesta: ')
while respuesta_4 not in ('a', 'b', 'c', 'd'):
      respuesta_4 = input('Debes responder a, b, c, o d. Ingresa nuevamente tu respuesta: ')
for numero_carga in range(3, -1, -1):
    print(f'\r{numero_carga}', end = '')
    time.sleep(1)  
if respuesta_4 == 'a':
 print(RED+'INCORRECTO', nombre, 'Spiderman tuvo contacto con la radiacion, asi obtuvo sus poderes'+RESET) 
 puntaje = puntaje - 1
elif respuesta_4 == 'b':
 print(RED+'INCORRECTO', nombre, 'Night thrasher es un humano con conocimientos de combate'+RESET) 
 puntaje = puntaje - 1
elif respuesta_4 == 'd':
 print(RED+'INCORRECTO', nombre, 'Crystal es un inhumano'+RESET) 
 puntaje = puntaje - 1
else:
 puntaje += 10 
 print(GREEN+'\n ¡MUY BIEN', nombre, '!'+RESET)
 print(MAGENTA+'\n TU MAYOR PUNTAJE OBTENIDO ES', puntaje,''+RESET)
  
 print('\n Espero',nombre , 'que la hayas pasado muy bien jugando.')
