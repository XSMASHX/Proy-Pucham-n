import pygame, random
import sys
import os
from PIL import Image

pygame.init()

# Dimensiones de la pantalla
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("PUCHAMON! 🔥💧🌱")

# Cargar imagen del menú inicial
background = pygame.image.load("img/imagen prueba.png").convert()

# Estado inicial
state = "menu"  # 'menu', 'animating', 'next_menu', 'game'

# Cargar el GIF con Pillow
gif_path = "animaciones/animacion prueba.gif"
gif = Image.open(gif_path)
gif_frames = []
try:
    while True:
        gif_frames.append(gif.copy())
        gif.seek(len(gif_frames))  # Ir al siguiente cuadro
except EOFError:
    pass  # Fin del GIF

# Convertir los cuadros del GIF a un formato que Pygame pueda usar
converted_frames = [pygame.image.fromstring(frame.tobytes(), frame.size, frame.mode) for frame in gif_frames]

animation_index = 0
animation_speed = 0.08  # Controlar la velocidad de la animación
animation_timer = 0

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fuentes
font = pygame.font.SysFont("arial", 30)

# Variables del juego
mascota = None
vidas_mascota = 100
vidas_enemigo = 100
mensaje = ""

# Función para mostrar texto en la pantalla
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

# Función para generar ataque enemigo
def generar_ataque_enemigo():
    return random.choice(["FUEGO🔥", "AGUA💧", "TIERRA🌱"])

# Función para calcular el resultado del ataque
def calcular_resultado(ataque, enemigo_ataque):
    if ataque == enemigo_ataque:
        return "EMPATE"
    elif (ataque == "FUEGO" and enemigo_ataque == "TIERRA") or \
         (ataque == "AGUA" and enemigo_ataque == "FUEGO") or \
         (ataque == "TIERRA" and enemigo_ataque == "AGUA"):
        return "GANA"
    else:
        return "PIERDE"

# Ciclo principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if state == "menu" and event.key == pygame.K_RETURN:
                state = "animating"  # Cambiar al estado de animación
            elif state == "next_menu":
                if mascota is None:
                    if event.key == pygame.K_1:
                        mascota = "Hipodoge"
                    elif event.key == pygame.K_2:
                        mascota = "Capipepo"
                    elif event.key == pygame.K_3:
                        mascota = "Ratigueya"
                else:
                    if event.key == pygame.K_f:
                        ataque = "FUEGO"
                    elif event.key == pygame.K_a:
                        ataque = "AGUA"
                    elif event.key == pygame.K_t:
                        ataque = "TIERRA"
                    else:
                        ataque = None
                    
                    if ataque:
                        enemigo_ataque = generar_ataque_enemigo()
                        resultado = calcular_resultado(ataque, enemigo_ataque)
                        
                        if resultado == "GANA":
                            vidas_enemigo -= 5
                            mensaje = f"Tu mascota atacó con {ataque}, el enemigo atacó con {enemigo_ataque} - GANASTE 🎉"
                        elif resultado == "PIERDE":
                            vidas_mascota -= 5
                            mensaje = f"Tu mascota atacó con {ataque}, el enemigo atacó con {enemigo_ataque} - PERDISTE 😢"
                        else:
                            mensaje = f"Tu mascota atacó con {ataque}, el enemigo atacó con {enemigo_ataque} - EMPATE 🤝"
                        
                        if vidas_mascota == 0:
                            mensaje = "Perdiste todas tus vidas. ¡Juego terminado!"
                        elif vidas_enemigo == 0:
                            mensaje = "El enemigo ha sido derrotado. ¡Ganaste!"
    
    # Renderizar según el estado actual
    if state == "menu":
        screen.blit(background, [0, 0])  # Mostrar el menú inicial

    elif state == "animating":
        if animation_index < len(converted_frames):
            animation_timer += animation_speed
            if animation_timer >= 1:
                animation_timer = 0
                screen.blit(converted_frames[animation_index], [0, 0])
                animation_index += 1
        else:
            state = "next_menu"  # Pasar al siguiente menú después de la animación

    elif state == "next_menu":
        screen.fill(WHITE)  # Fondo blanco para el menú de selección de mascota
        
        if mascota is None:
            draw_text("Elige tu mascota (1: Hipodoge, 2: Capipepo, 3: Ratigueya)", font, BLACK, screen, screen_width // 2, screen_height // 2)
        else:
            draw_text(f"Tu mascota: {mascota}", font, BLACK, screen, screen_width // 2, 50)
            draw_text(f"Tu mascota tiene {vidas_mascota} vidas", font, BLACK, screen, screen_width // 2, 100)
            draw_text(f"El enemigo tiene {vidas_enemigo} vidas", font, BLACK, screen, screen_width // 2, 150)
            draw_text("Presiona F para Fuego, A para Agua, T para Tierra", font, BLACK, screen, screen_width // 2, 200)
            draw_text(mensaje, font, BLACK, screen, screen_width // 2, 300)

    pygame.display.flip()

pygame.quit()
