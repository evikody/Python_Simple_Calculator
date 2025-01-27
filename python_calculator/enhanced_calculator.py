import pygame
import sys
import re

# Initialize pygame
pygame.init()

# Set up screen dimensions and caption
WIDTH, HEIGHT = 580, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Calculator")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)

# Set font
font = pygame.font.Font(None, 50)
history_font = pygame.font.Font(None, 30)

# Initialize calculator state
input_text = ""
result_text = ""

# Store calculation history
history = []

# Define a function to draw buttons
def draw_button(text, x, y, w, h):
    pygame.draw.rect(screen, GRAY, (x, y, w, h), border_radius=8)
    label = font.render(text, True, BLACK)
    screen.blit(label, (x + w // 2 - label.get_width() // 2, y + h // 2 - label.get_height() // 2))

# Define a function to prevent invalid expressions
def sanitize_input(input_text):
    # Remove invalid consecutive operators
    input_text = re.sub(r'[+\-*/^]{2,}', '', input_text)
    # Prevent starting with invalid operators
    if input_text and input_text[0] in '+*/^':
        input_text = input_text[1:]
    return input_text

# Define a function to parse and adjust the expression for additional features
def parse_expression(expression):
    expression = expression.replace('^', '**')  # Handle power
    expression = expression.replace('%', '/100')  # Convert percentage
    # Add implicit multiplication (e.g., 2(3+1) -> 2*(3+1))
    expression = re.sub(r'(\d)(\()', r'\1*(', expression)
    return expression

# Define a function to format result (truncate or convert to scientific notation)
def format_result(result):
    if len(result) > 10:  # Assume 10 is the max character length
        try:
            result = f"{float(result):.8g}"  # Convert to scientific notation
        except:
            pass
    return result

# Define a function to evaluate the input expression
def calculate(expression):
    try:
        parsed = parse_expression(expression)
        result = str(eval(parsed))
        return format_result(result)
    except:
        return "Error"

# Define a function to add calculations to history
def add_to_history(input_text, result_text):
    # Modify the history list to global
    global history
    if len(history) >= 5:  # Keep only the last 5 entries
        history.pop(0)
    history.append(f"{input_text} = {result_text}")

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

    # Display the history
    pygame.draw.rect(screen, (220, 220, 220), (0, 150, WIDTH, 120))  # Background for history
    for i, entry in enumerate(history):
        history_surface = history_font.render(entry, True, BLACK)
        screen.blit(history_surface, (20, 160 + i * 25))

    # c.) Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # If the user presses a key after calculating a result, clear the input for a new calculation
        elif event.type == pygame.KEYDOWN:
            if result_text:  # Reset input if there's a result
                input_text = ""
                result_text = ""
            # Update during calculation
            elif event.key == pygame.K_RETURN:
                input_text = sanitize_input(input_text)
                result_text = calculate(input_text)
                add_to_history(input_text, result_text)
                input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                key = event.unicode
                if key in '0123456789+-*/.^':  # Include ^ in the allowed keys
                    input_text += key

    # d.) Define buttons and draw them
    button_texts = [
        ('7', 50, 300), ('8', 150, 300), ('9', 250, 300), ('/', 350, 300),
        ('4', 50, 400), ('5', 150, 400), ('6', 250, 400), ('*', 350, 400),
        ('1', 50, 500), ('2', 150, 500), ('3', 250, 500), ('-', 350, 500),
        ('0', 50, 600), ('.', 150, 600), ('+', 250, 600), ('=', 350, 600),
        ('^', 450, 300),  # Add the caret button for power
    ]

    for (text, x, y) in button_texts:
        draw_button(text, x, y, 80, 80)

    # e.) Update the display
    pygame.display.flip()
    pygame.time.delay(30)

# Quit pygame
pygame.quit()
sys.exit()
