import serial
import pygame
 
arduino = serial.Serial('COM9', 9600)
 
pygame.init()                                      #pygame lo utilizamos para crear una interfaz grafica la cual detectara que teclas presionamos y cuanto las mantenemos presionadas 
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Tanque!')
pygame.mouse.set_visible(1)
 
val = 's'                               # le damos un valor cualquiera a la variable pues necesitamos que se inicie el bucle 

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
                    arduino.close()
            if event.type == pygame.KEYUP:                  # en el momento que dejamos de precionar una de todas las teclas el robot se detiene
                arduino.write(b's')