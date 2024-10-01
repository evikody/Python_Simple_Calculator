import pygame
import sys

# Initialize pygame
pygame.init()

# Set up screen dimensions and caption
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Calculator")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)

# Set font
font = pygame.font.Font(None, 50)

# Initialize calculator state
input_text = ""
result_text = ""

# Define a function to draw buttons
def draw_button(text, x, y, w, h):
    pygame.draw.rect(screen, GRAY, (x, y, w, h), border_radius=8)
    label = font.render(text, True, BLACK)
    screen.blit(label, (x + w // 2 - label.get_width() // 2, y + h // 2 - label.get_height() // 2))

# Define a function to evaluate the input expression
def calculate(expression):
    try:
        return str(eval(expression))
    except:
        return "Error"

# Enter the game loop
running = True
while running:
    # a.) Fill the screen with background color
    screen.fill(WHITE)

    # b.) Render input text and result
    input_surface = font.render(input_text, True, BLACK)
    screen.blit(input_surface, (20, 50))

    result_surface = font.render(result_text, True, GREEN)
    screen.blit(result_surface, (20, 100))

    # c.) Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                result_text = calculate(input_text)
                input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                key = event.unicode
                if key in '0123456789+-*/.':
                    input_text += key
                    