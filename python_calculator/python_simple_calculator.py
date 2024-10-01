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