import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da janela
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Captura de Input com Pygame")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonte
font = pygame.font.Font(None, 74)

# Variáveis de controle de input
input_active = False
user_text = ""

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Ativa o campo de input se o usuário clicar dentro de uma área específica
            if input_box.collidepoint(event.pos):
                input_active = True
            else:
                input_active = False
        if event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN:
                print(f"Texto inserido: {user_text}")
                user_text = ""
            elif event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode

    # Desenha a tela
    screen.fill(WHITE)

    # Desenha o texto
    text_surface = font.render(user_text, True, BLACK)
    screen.blit(text_surface, (50, 50))

    # Desenha a caixa de input
    input_box = pygame.Rect(50, 50, 700, 100)
    pygame.draw.rect(screen, BLACK, input_box, 2)

    pygame.display.flip()

pygame.quit()
sys.exit()
