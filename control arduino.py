import serial                                      #serial es la libreria la cual nos permite comunicarnos con arduino
import pygame                                      #pygame es una libreria pensada para crear videojuegos pero en este caso nos resulta util
 
arduino = serial.Serial('COM9', 9600)              #Definimos que arduino sera una variable que contendra el puerto (COM9) y la frecuencia (9600 baudios) con la cual nos comunicaremos
                                                   #con el arduino
pygame.init()                                      #pygame lo utilizamos para crear una interfaz grafica la cual detectara que teclas presionamos y cuanto las mantenemos presionadas 
screen = pygame.display.set_mode((640, 480))       #Con esta linea de codigo definimos el alto y ancho de nuestra ventana
pygame.display.set_caption('Tanque!')              #Con esta linea de codigo le colocamos un nombre a la ventana que se creara
pygame.mouse.set_visible(1)                        #Nos deja elegir si se muestra el puntero del raton mientras este sobre la ventana
 
val = 's'                               # le damos un valor cualquiera a la variable pues necesitamos que se inicie el bucle y se quede abierto a menos que esta variable se convierta en stop

while val != 'stop':                #mientras que el valor que ingresemos no sea stop se va a repetir el bucle
    events = pygame.event.get()
    for event in events:
            if event.type == pygame.KEYDOWN:            #pygame.KEYDOWN detecta que teclas estan siendo presionadas en el momento que sucede si es la flecha de arriba o abajo enviara la señal
                if event.key == pygame.K_UP:            #Arduino se mueve hacia adelante al precionar la flecha de arriba
                        arduino.write(b'r')
                elif event.key == pygame.K_LEFT:        #Arduino se mueve hacia la izquierda al presionar la flecha izquierda
                        arduino.write(b'i')
                elif event.key == pygame.K_RIGHT:           #Arduino se mueve hacia la derecha al presionar la flecha derecha
                    arduino.write(b'd')
                elif event.key == pygame.K_DOWN:            #Arduino se mueve hacia atras al presionar la flecha de abajo
                    arduino.write(b'a')
                elif event.key == pygame.K_ESCAPE:          #Al presionar la tecla escape cerramos el arduino 
                    val = 'stop'
                    arduino.close()                         #arduino.close() cierra el puerto de comunicacion que estamos utilizando para enviarle informacion a arduino
            if event.type == pygame.KEYUP:                  #pygame.KEYUP detecta cuando dejamos de pulsar una tecla y
                arduino.write(b's')                         #en el momento que dejamos de presionar una de las teclas el robot se detiene