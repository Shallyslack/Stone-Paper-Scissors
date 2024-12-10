import pygame
import random
import os
pygame.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Stone-Paper-Scissors Game")
font = pygame.font.Font(None, 40)
button_font = pygame.font.Font(None, 30)
PINK = (255, 105, 180)
WHITE = (255, 255, 255)
LIGHT_BLUE = (173, 216, 230)
HIGHLIGHT_COLOR = (200, 200, 255)
HEADING_COLOR = (255, 255, 255)
PLAYER_COLOR = (50, 150, 50)
COMPUTER_COLOR = (200, 50, 50)
RESULT_COLOR = (255, 165, 0)
HEADING_BG_COLOR = (255, 105, 180)
OPTION_COLOR = (255, 255, 255)  
OPTION_BOX_COLOR = (255, 105, 180)  
print(os.getcwd())
stone_img = pygame.image.load("Stone-Paper-Scissors/stone.png")
paper_img = pygame.image.load("c:/Users/DELL/OneDrive/Documents/gui/Stone-Paper-Scissors/paper.png")
scissors_img = pygame.image.load("c:/Users/DELL/OneDrive/Documents/gui/Stone-Paper-Scissors/scissors.png")

stone_img = pygame.transform.scale(stone_img, (100, 100))
paper_img = pygame.transform.scale(paper_img, (100, 100))
scissors_img = pygame.transform.scale(scissors_img, (100, 100))

choices = ["Stone", "Paper", "Scissors"]
button_width = 150
button_height = 50
buttons = {
    "Stone": pygame.Rect(50, 550, button_width, button_height),
    "Paper": pygame.Rect(250, 550, button_width, button_height),
    "Scissors": pygame.Rect(450, 550, button_width, button_height)
}

def render_text(text, font, color, position):
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, position)

def get_computer_choice():
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a draw!"
    elif (player_choice == "Stone" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Stone") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

def draw_gradient_background():
    for y in range(700):
        color = (173 + int(82 * (y / 700)), 216, 230)
        pygame.draw.line(screen, color, (0, y), (700, y))

def main():
    running = True
    player_choice = None
    computer_choice = None
    result = None
    highlight_button = None

    heading_text = "Stone Paper Scissors Game"
    heading_width, heading_height = font.size(heading_text)
    heading_pos = (screen.get_width() // 2 - heading_width // 2, 50)
    heading_box = pygame.Rect(heading_pos[0] - 20, heading_pos[1] - 10, heading_width + 40, heading_height + 20)

    choose_option_text = "CHOOSE YOUR OPTION"
    choose_option_width, choose_option_height = button_font.size(choose_option_text)
    choose_option_pos = (screen.get_width() // 2 - choose_option_width // 2, 350)  

    choose_option_box = pygame.Rect(choose_option_pos[0] - 20, choose_option_pos[1] - 10, choose_option_width + 40, choose_option_height + 20)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttons["Stone"].collidepoint(event.pos):
                    player_choice = "Stone"
                    computer_choice = get_computer_choice()
                    result = determine_winner(player_choice, computer_choice)
                elif buttons["Paper"].collidepoint(event.pos):
                    player_choice = "Paper"
                    computer_choice = get_computer_choice()
                    result = determine_winner(player_choice, computer_choice)
                elif buttons["Scissors"].collidepoint(event.pos):
                    player_choice = "Scissors"
                    computer_choice = get_computer_choice()
                    result = determine_winner(player_choice, computer_choice)

            if event.type == pygame.MOUSEMOTION:
                if buttons["Stone"].collidepoint(event.pos):
                    highlight_button = "Stone"
                elif buttons["Paper"].collidepoint(event.pos):
                    highlight_button = "Paper"
                elif buttons["Scissors"].collidepoint(event.pos):
                    highlight_button = "Scissors"
                else:
                    highlight_button = None

        draw_gradient_background()
        pygame.draw.rect(screen, HEADING_BG_COLOR, heading_box)
        render_text(heading_text, font, HEADING_COLOR, heading_pos)

        if not result:
            pygame.draw.rect(screen, OPTION_BOX_COLOR, choose_option_box)  
            render_text(choose_option_text, button_font, OPTION_COLOR, choose_option_pos)

        for key, rect in buttons.items():
            if key == highlight_button:
                pygame.draw.rect(screen, HIGHLIGHT_COLOR, rect)  
            else:
                pygame.draw.rect(screen, PINK, rect)

        screen.blit(stone_img, (buttons["Stone"].x + 25, buttons["Stone"].y - 100))
        screen.blit(paper_img, (buttons["Paper"].x + 25, buttons["Paper"].y - 100))
        screen.blit(scissors_img, (buttons["Scissors"].x + 25, buttons["Scissors"].y - 100))

        render_text("Stone", button_font, WHITE, (buttons["Stone"].x + 45, buttons["Stone"].y + 10))
        render_text("Paper", button_font, WHITE, (buttons["Paper"].x + 45, buttons["Paper"].y + 10))
        render_text("Scissors", button_font, WHITE, (buttons["Scissors"].x + 35, buttons["Scissors"].y + 10))

        
        if player_choice and computer_choice:
            render_text(f"Player: {player_choice}", font, PLAYER_COLOR, (50, 100))
            render_text(f"Computer: {computer_choice}", font, COMPUTER_COLOR, (50, 150))

        
        if result:
            render_text(result, font, RESULT_COLOR, (50, 200))

        pygame.display.update()

    pygame.quit()


main()
