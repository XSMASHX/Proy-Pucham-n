import pygame, sys
import random
pygame.init()

# Dimensiones de la pantalla y cerrar pantalla
screen = pygame.display.set_mode([1280, 720])
pygame.display.set_caption("PUCHAMON! 🔥💧🌱")

# Cargar la imagen de fondo
background = pygame.image.load(r"C:\Users\usuario\Desktop\Kevin\Algoritmos\Proyecto Puchamon\img\imagen prueba.png").convert()


run = True
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  # Aquí usamos "=" para asignar el valor

    # Dibujar la imagen de fondo en la pantalla
    screen.blit(background, (300, 200))  # Corregido formato de las coordenadas

    pygame.display.flip()  # Actualizar la pantalla
    
pygame.quit()
