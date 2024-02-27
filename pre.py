import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, K_RIGHT, K_LEFT

# Configuración inicial
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Presentación en Python")

# Colores
white = (255, 255, 255)

# Contenido de la presentación
slides = ["Slide 1", "Slide 2", "Slide 3", "Slide 4"]
current_slide = 0

# Configuración de la fuente
font = pygame.font.Font(None, 36)

# Bucle principal
running = True
while running:
    screen.fill(white)

    # Dibuja el contenido de la presentación
    text = font.render(slides[current_slide], True, (0, 0, 0))
    screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))

    pygame.display.flip()

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                current_slide = (current_slide + 1) % len(slides)
            elif event.key == K_LEFT:
                current_slide = (current_slide - 1) % len(slides)

# Finaliza Pygame
pygame.quit()
