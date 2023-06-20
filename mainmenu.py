import os
import pygame
from charactercreator import charactercreator

def mainmenu():
    pygame.init()

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Horse Game")

    image_filename = "mainbackground.png"
    image_path = os.path.join("gameimages", image_filename)
    background_image = pygame.image.load(image_path)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 100 <= mouse_pos[0] <= 300 and 200 <= mouse_pos[1] <= 230:
                    charactercreator()

        screen.blit(background_image, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), (100, 200, 200, 30))

        font = pygame.font.Font(None, 24)
        new_game_text = font.render("New Game", True, (255, 255, 255))
        screen.blit(new_game_text, (120, 205))

        pygame.display.flip()

    pygame.quit()
    exit()

if __name__ == "__main__":
    main_menu()
