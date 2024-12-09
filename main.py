import pygame

pygame.init()
screen = pygame.display.set_mode((700,700))

running = True
font = pygame.font.Font(None, 24)
button_surface = pygame.Surface((150, 50))

# Render text on the button
text = font.render("Click Me", True, (0, 0, 0))
text_rect = text.get_rect(center=(button_surface.get_width()/2, button_surface.get_height()/2))


# Create a pygame.Rect object that represents the button's boundaries
button_rect = pygame.Rect(125, 125, 150, 50)


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("#FCFFC1")
    pygame.draw.rect(screen, "black", button_rect)

    pygame.display.update()

pygame.quit()