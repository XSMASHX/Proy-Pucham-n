import pygame
import random

# Inicializamos Pygame
pygame.init()

# Inicializamos el objeto Clock para controlar los FPS
clock = pygame.time.Clock()

# Definimos las dimensiones de la ventana
screen_width = 1080
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# Título del juego
pygame.display.set_caption("Puchamón")

# Cargar imagenes
start_screen_background = pygame.image.load('Proy-Pucham-n-main/Proy-Pucham-n-main/Proyecto Puchamon/img/imagen prueba.png')
start_batalla = pygame.image.load('Proy-Pucham-n-main/Proy-Pucham-n-main/Proyecto Puchamon/img/batallapoke.png')
start_personajesmenú = pygame.image.load('Proy-Pucham-n-main/Proy-Pucham-n-main/Proyecto Puchamon/img/menú personajes.png')
Gabs = pygame.image.load('Proy-Pucham-n-main/Proy-Pucham-n-main/Proyecto Puchamon/Personajes/Gabs.png')
Mark = pygame.image.load('Proy-Pucham-n-main/Proy-Pucham-n-main/Proyecto Puchamon/Personajes/Mark.png')
Lavs = pygame.image.load('Proy-Pucham-n-main/Proy-Pucham-n-main/Proyecto Puchamon/Personajes/Lavs.png')
Kevo = pygame.image.load('Proy-Pucham-n-main/Proy-Pucham-n-main/Proyecto Puchamon/Personajes/Kevo.png')
Anth = pygame.image.load('Proy-Pucham-n-main/Proy-Pucham-n-main/Proyecto Puchamon/Personajes/Anth.png')
Jopa = pygame.image.load('Proy-Pucham-n-main/Proy-Pucham-n-main/Proyecto Puchamon/Personajes/Jopa.png')
Carmin = pygame.image.load('Proy-Pucham-n-main/Proy-Pucham-n-main/Proyecto Puchamon/Personajes/Carmin.png')
Drenaz = pygame.image.load('Proy-Pucham-n-main/Proy-Pucham-n-main/Proyecto Puchamon/Personajes/Drenaz.png')
frames_ataque_enemigo = [
    pygame.image.load('Proy-Pucham-n-main/Proy-Pucham-n-main/Proyecto Puchamon/Personajes/ataque poke1.png'),
    pygame.image.load('Proy-Pucham-n-main/Proy-Pucham-n-main/Proyecto Puchamon/Personajes/ataque poke2.png'),
    pygame.image.load('Proy-Pucham-n-main/Proy-Pucham-n-main/Proyecto Puchamon/Personajes/ataque poke3.png')
]
start_screen_background = pygame.transform.scale(start_screen_background, (screen_width, screen_height))



# Definimos los colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Fuente para el texto
font = pygame.font.Font(None, 36)

# Salud inicial de los personajes
MAX_HEALTH = 100


# Nueva variable para almacenar el personaje seleccionado
personaje_seleccionado = "Gabs"  # Puedes cambiarlo según el personaje que elija el jugador

# Diccionario de imágenes de personajes
imagenes_personajes = {
    "Gabs": Gabs,
    "Mark": Mark,
    "Lav": Lavs,
    "Kevo": Kevo,
    "Anth": Anth,
    "Jopa": Jopa,
    "Carmin": Carmin,
    "Drenaz": Drenaz
}


# Variables globales para el estado de los ataques
jugador_boost_daño = 0
turnos_boost = 0  # Controla cuántos turnos dura el boost de daño del jugador
enemigo_boost_daño = 0
turnos_boost_enemigo = 0  # Controla cuántos turnos dura el boost de daño del enemigo
enemigo_reduce_daño = False  # Indica si el enemigo está bajo el efecto de reducción de daño
turnos_reducir_daño = 0  # Controla cuántos turnos durará la reducción de daño
jugador_invalido = False  # Indica si el jugador está invalidado
enemigo_invalido = False  # Indica si el enemigo está invalidado


# Personajes y sus naturalezas y ataques
characters = {
    "Gabs": {"naturaleza": "Fuerte", "ataques": ["Llamazo", "Manazo", "Caliente", "Inválido"]},
    "Mark": {"naturaleza": "Firme", "ataques": ["Botellazo", "Manazo", "Inválido", "Gruñir"]},
    "Lav": {"naturaleza": "Equilibrado", "ataques": ["Motivación", "Llamazo", "Manazo", "Facto"]},
    "Kevo": {"naturaleza": "Fuerte", "ataques": ["Facto", "Llamazo", "Beso", "Motivación"]},
    "Anth": {"naturaleza": "Ágil", "ataques": ["Manazo", "Beso", "Facto", "Inválido"]},
    "Jopa": {"naturaleza": "Firme", "ataques": ["Gruñir", "Beso", "Caliente", "Botellazo"]},
    "Carmin": {"naturaleza": "Ágil", "ataques": ["Beso", "Manazo", "Caliente", "Motivación"]},
    "Drenaz": {"naturaleza": "Equilibrado", "ataques": ["Inválido", "Manazo", "Botellazo", "Gruñir"]}
}

# Definimos los ataques y su efecto
ataques = {
    "Llamazo": {"naturaleza": "Fuerte", "daño": 10, "descripcion": "Quita 10 de vida, 15 si la naturaleza del atacante es la misma"},
    "Caliente": {"naturaleza": "Fuerte", "daño": 0, "descripcion": "Hace que el atacante se enfuerza y haga un 40% más de daño por los dos turnos siguientes"},
    "Inválido": {"naturaleza": "Firme", "daño": 0, "descripcion": "Invalida al enemigo por un turno, no puede atacar"},
    "Manazo": {"naturaleza": "Neutro", "daño": 10, "descripcion": "Quita 10 de vida al enemigo"},
    "Botellazo": {"naturaleza": "Equilibrado", "daño": 20, "descripcion": "Tiene un 55% de probabilidad de acertar, si acierta, quita 20 puntos de vida"},
    "Gruñir": {"naturaleza": "Ágil", "daño": 0, "descripcion": "Intimida al enemigo y hace que sus ataques hagan 10% menos daño por los dos turnos siguientes"},
    "Motivación": {"naturaleza": "Firme", "daño": -10, "descripcion": "Cura 10 puntos de vida al atacante, 50% de probabilidad de curar 15 si la naturaleza es compatible"},
    "Facto": {"naturaleza": "Equilibrado", "daño": 10, "descripcion": "Quita 10 de vida al enemigo, 15 si la naturaleza es compatible"},
    "Beso": {"naturaleza": "Ágil", "daño": 5, "descripcion": "Quita 5 puntos de vida y cura 5 puntos al atacante, hay 50% de probabilidad de que quite 10 y cure 10 si la naturaleza es compatible"}
}


# Función para mostrar el texto en pantalla
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    surface.blit(text_obj, (x, y))

# Función para calcular daño basado en naturaleza y ataque
def calcular_daño(ataque, nombre_atacante, nombre_defensor, es_jugador=True):
    global jugador_boost_daño, turnos_boost
    global enemigo_boost_daño, turnos_boost_enemigo
    global enemigo_reduce_daño, turnos_reducir_daño
    global jugador_invalido, enemigo_invalido
    global jugador_hp, enemigo_hp  # Asegúrate de tener estas variables globales

    base_daño = ataques[ataque]["daño"]

    # Ataque Llamazo
    if ataque == "Llamazo":
        if characters[nombre_atacante]["naturaleza"] == "Fuerte":
            base_daño = 15
        else:
            base_daño = 10
    
    # Aplicar "Caliente" para el jugador
    if es_jugador and turnos_boost > 0:
        base_daño += base_daño * jugador_boost_daño  # Aumentar el daño en un 40%
        turnos_boost -= 1  # Reducir el contador de turnos

    # Aplicar "Caliente" para el enemigo
    elif not es_jugador and turnos_boost_enemigo > 0:
        base_daño += base_daño * enemigo_boost_daño  # Aumentar el daño en un 40%
        turnos_boost_enemigo -= 1  # Reducir el contador de turnos

    # Ataque Caliente (no causa daño directo pero activa el boost)
    if ataque == "Caliente":
        if es_jugador:
            turnos_boost = 2  # Reiniciar el contador de turnos para el jugador
            jugador_boost_daño = 0.4  # Aumento del 40% en daño
        else:
            turnos_boost_enemigo = 2  # Reiniciar el contador de turnos para el enemigo
            enemigo_boost_daño = 0.4  # Aumento del 40% en daño
        return 0, f"{nombre_atacante} usó {ataque} y su daño aumentará durante 2 turnos."

    if ataque == "Inválido":
        if random.random() < 0.5:  # 50% de probabilidad de acertar
            if es_jugador:
                enemigo_invalido = True  # Invalida al enemigo por 1 turno
                return 0, f"{nombre_atacante} usó {ataque} y ha invalidado a {nombre_defensor} por un turno."
            else:
                jugador_invalido = True  # Invalida al jugador por 1 turno
                return 0, f"{nombre_atacante} usó {ataque} y ha invalidado a {nombre_defensor} por un turno."
        else:
            return 0, f"{ataque} falló y no invalidó a {nombre_defensor}."

    # Ataque Manazo
    if ataque == "Manazo":
        base_daño = 10

    if ataque == "Botellazo":
        if random.random() < 0.55:  # 55% de probabilidad de acertar
            return 20, f"{ataque} acertó y causó 20 puntos de daño a {nombre_defensor}."
        else:
            return 0, f"{ataque} falló y no causó daño."
    
    if ataque == "Gruñir":
        if enemigo_reduce_daño:
            turnos_reducir_daño = 2  # Reiniciar el contador de turnos si ya está activo
        else:
            enemigo_reduce_daño = True  # Activar la reducción de daño si no estaba activa
            turnos_reducir_daño = 2  # Duración de 2 turnos
        return 0, f"{nombre_atacante} intimidó a {nombre_defensor}, reduciendo el daño que causará en los próximos turnos."

    # Aplicar reducción de daño si "Gruñir" está activo
    if not es_jugador and enemigo_reduce_daño and turnos_reducir_daño > 0:
        base_daño *= 0.6  # Reduce el daño en un 40%
        turnos_reducir_daño -= 1  # Reducir la duración del efecto en 1 turno

        if turnos_reducir_daño == 0:
            enemigo_reduce_daño = False  # Desactivar la reducción de daño cuando el efecto termina
    
    if ataque == "Motivación":
        if characters[nombre_atacante]["naturaleza"] == "Firme":
            cura = 15  # Cura 15 puntos si la naturaleza es compatible
        else:
            cura = 10  # Cura 10 puntos

        if es_jugador:
            jugador_hp = min(jugador_hp + cura, 100)  # Asegúrate de que no sobrepase el máximo (100)
        else:
            enemigo_hp = min(enemigo_hp + cura, 100)  # Asegúrate de que no sobrepase el máximo (100)

        return 0, f"{nombre_atacante} usó {ataque} y curó {cura} puntos de vida."

    # Ataque Facto
    if ataque == "Facto":
        if characters[nombre_atacante]["naturaleza"] == "Equilibrado":
            base_daño = 15
        else:
            base_daño = 10

    if ataque == "Beso":
        if characters[nombre_atacante]["naturaleza"] == "Ágil":
            return 15, f"{ataque} causó 15 puntos de daño a {nombre_defensor}."
        else:
            return 10, f"{ataque} causó 10 puntos de daño a {nombre_defensor}."
    
        # Devolver el daño final calculado
    return base_daño, f"{ataque} causó {int(base_daño)} puntos de daño a {nombre_defensor}."

def mostrar_ataques(ataques_jugador, screen_width, y):
    # Calculamos el centro de la pantalla
    for i, ataque in enumerate(ataques_jugador):
        columna = i % 2  # 0 para la primera columna, 1 para la segunda columna
        fila = i // 2  # Divide los ataques en filas (2 ataques por fila)
        
        # Calculamos la posición para centrar
        ataque_text = f'{i + 1}. {ataque}'
        text_surface = font.render(ataque_text, True, BLACK)
        text_width = text_surface.get_width()
        x = (screen_width // 2) - 200 + columna * 250  # Ajustar las columnas
        
        # Dibujamos el ataque centrado en la posición 'x'
        draw_text(ataque_text, font, BLACK, screen, x, y + fila * 40)


#animación ataque
def animar_ataque(frames, x, y):
    for frame in frames:
        screen.blit(frame, (x, y))
        pygame.display.flip()
        pygame.time.delay(100)  # Retraso entre frames



# Función para mostrar la barra de salud
def mostrar_barra_salud(nombre_jugador, hp, x, y):
    if hp < 0:
        hp = 0
    largo_barra = 200
    barra = (hp / MAX_HEALTH) * largo_barra
    pygame.draw.rect(screen, RED, (x, y, largo_barra, 25))
    pygame.draw.rect(screen, GREEN, (x, y, barra, 25))

# Función de batalla
def batalla(jugador, enemigo):
    global personaje_seleccionado
    global enemigo_invalido  # Usar la variable global enemigo_invalido
    global jugador_invalido  # Usar la variable global jugador_invalido
    global jugador_hp, enemigo_hp  # Para que la curación se aplique correctamente

    jugador_hp = MAX_HEALTH
    enemigo_hp = MAX_HEALTH

    turno_jugador = True
    batalla_terminada = False
    mensaje = ""

    while not batalla_terminada:
        screen.blit(start_batalla, (0, 0))

        # Mostrar la imagen del personaje seleccionado
        screen.blit(imagenes_personajes[jugador], (60, 250))  # Ajusta la posición según necesites
        screen.blit(imagenes_personajes[enemigo], (750, 250))  # Posición del enemigo
        
        #barras de salud
        mostrar_barra_salud(jugador, jugador_hp, 20, 60)   # Ajusta la posición según necesites
        mostrar_barra_salud(enemigo, enemigo_hp, 800, 60)
        
        # Mostrar salud de ambos personajes
        draw_text(f'{jugador}: {jugador_hp} HP', font, GREEN, screen, 20, 20)
        draw_text(f'{enemigo}: {enemigo_hp} HP', font, RED, screen, 800, 20)
        
        if turno_jugador:
            if jugador_invalido:
                mensaje = f'{jugador} está invalidado y no puede atacar este turno.'
                # Limpiar el área del mensaje antes de dibujar el texto
                pygame.draw.rect(screen, WHITE, (100, screen_height - 100, 760, 80))  # Limpiar el área
                draw_text_wrapped(mensaje, font, BLACK, screen, 100, screen_height - 200, 760)
                pygame.display.flip()
                pygame.time.wait(2000)  # Espera 2 segundos para mostrar el mensaje
                jugador_invalido = False  # Restablecemos el estado de invalidez
                turno_jugador = False  # Cambiamos el turno al enemigo
            else:
                ataques_jugador = characters[jugador]["ataques"]
                mostrar_ataques(ataques_jugador, screen_width, screen_height - 100)

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                            ataque_index = event.key - pygame.K_1
                            ataque_seleccionado = ataques_jugador[ataque_index]
                            
                            daño, mensaje = calcular_daño(ataque_seleccionado, jugador, enemigo, es_jugador=True)
                            animar_ataque(frames_ataque_enemigo, 60, 250)
                            
                            # Aplicar curación o daño según el ataque
                            if ataque_seleccionado == "Motivación":
                                jugador_hp = min(jugador_hp - daño, 100)  # Aplicar curación hasta un máximo de 100
                            else:
                                enemigo_hp -= daño
                                enemigo_hp = max(0, enemigo_hp)  # Asegurarse de que no baje de 0

                            mensaje = f'{jugador} usó {ataque_seleccionado} contra {enemigo}. {mensaje}'
                            # Limpiar el área del mensaje antes de dibujar el nuevo
                            pygame.draw.rect(screen, WHITE, (100, screen_height - 100, 760, 80))
                            draw_text_wrapped(mensaje, font, BLACK, screen, 100, screen_height - 100, 760)
                            pygame.display.flip()

                            pygame.time.wait(2000)  # Esperar 2 segundos para mostrar el mensaje del ataque

                            turno_jugador = False  # Cambia de turno

                            if enemigo_hp <= 0:
                                enemigo_hp = 0  # Mostrar la vida en cero antes de terminar
                                pygame.display.flip()
                                pygame.time.wait(2500)  # Esperar antes de finalizar la batalla
                                batalla_terminada = True
                                mensaje = f'{jugador} ganó la batalla!'
                            
                            pygame.time.wait(500)  # Pequeña pausa antes de continuar
        else:
            if not enemigo_invalido:  # Si el enemigo no está invalidado
                ataque_enemigo = random.choice(characters[enemigo]["ataques"])
                daño, mensaje = calcular_daño(ataque_enemigo, enemigo, jugador, es_jugador=False)
                animar_ataque(frames_ataque_enemigo, 750, 250)
                
                if ataque_enemigo == "Motivación":
                    enemigo_hp = min(enemigo_hp - daño, 100)  # Aplicar curación hasta un máximo de 100
                else:
                    jugador_hp -= daño
                    jugador_hp = max(0, jugador_hp)  # Asegurarse de que no baje de 0

                if ataque_enemigo == "Inválido" and random.random() < 0.5:  # 50% de probabilidad de acertar
                    jugador_invalido = True  # El jugador queda invalidado
                    mensaje += " El enemigo te ha invalidado y atacará de nuevo."
                    # Limpiar el área del mensaje antes de dibujar el nuevo
                    pygame.draw.rect(screen, WHITE, (100, screen_height - 100, 760, 80))
                    draw_text_wrapped(mensaje, font, BLACK, screen, 100, screen_height - 100, 760)
                    pygame.display.flip()
                    pygame.time.wait(2000)  # Espera para mostrar el mensaje

                    # El enemigo vuelve a atacar de inmediato si invalida al jugador
                    ataque_enemigo = random.choice(characters[enemigo]["ataques"])
                    daño, mensaje = calcular_daño(ataque_enemigo, enemigo, jugador, es_jugador=False)
                    if ataque_enemigo != "Motivación":
                        jugador_hp -= daño
                        jugador_hp = max(0, jugador_hp)  # Asegurarse de que no baje de 0
                else:
                    mensaje = f'{enemigo} usó {ataque_enemigo} contra {jugador}. {mensaje}'

                # Limpiar el área del mensaje antes de dibujar el nuevo
                pygame.draw.rect(screen, WHITE, (100, screen_height - 100, 760, 80))
                draw_text_wrapped(mensaje, font, BLACK, screen, 100, screen_height - 100, 760)
                pygame.display.flip()

                pygame.time.wait(2500)

                # Limpiar solo el área del mensaje
                pygame.draw.rect(screen, WHITE, (100, screen_height - 100, 760, 80))
                pygame.display.flip()
                pygame.time.wait(500)

                if jugador_hp <= 0:
                    jugador_hp = 0
                    batalla_terminada = True
                    mensaje = f'{enemigo} ganó la batalla!'
            else:
                enemigo_invalido = False  # Restablecer el estado de invalidez para el siguiente turno
            turno_jugador = True

        pygame.display.flip()
        clock.tick(60)


# Función para seleccionar personaje
def seleccionar_personaje():
    selected = False
    personaje_seleccionado = None
    while not selected:
        screen.blit(start_personajesmenú, (0, 0))
        draw_text('Selecciona tu personaje:', font, BLACK, screen, 20, 20)
        
        # Mostrar lista de personajes
        y = 100
        for i, personaje in enumerate(characters.keys()):
            draw_text(f'{i + 1}. {personaje}', font, BLACK, screen, 50, y)
            y += 40
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8]:
                    personaje_seleccionado = list(characters.keys())[event.key - pygame.K_1]
                    selected = True
    
    return personaje_seleccionado

# Función para seleccionar un enemigo aleatorio
def seleccionar_enemigo():
    enemigo = random.choice(list(characters.keys()))
    return enemigo

def draw_text_wrapped(text, font, color, surface, x, y, max_width):
    words = text.split(' ')
    lines = []
    current_line = []
    current_width = 0

    for word in words:
        word_surface = font.render(word, True, color)
        word_width, word_height = word_surface.get_size()
        if current_width + word_width <= max_width:
            current_line.append(word)
            current_width += word_width + font.size(' ')[0]
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_width = word_width + font.size(' ')[0]

    if current_line:
        lines.append(' '.join(current_line))

    for i, line in enumerate(lines):
        line_surface = font.render(line, True, color)
        surface.blit(line_surface, (x, y + i * font.get_height()))

# Bucle principal
def main():
    running = True
    while running:
        screen.blit(start_screen_background, (0, 0))
        draw_text("Presiona Enter para iniciar", font, BLACK, screen, 370, 350)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    jugador = seleccionar_personaje()
                    enemigo = seleccionar_enemigo()
                    estado = batalla(jugador, enemigo)
                    if estado == "menú":
                        continue

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
