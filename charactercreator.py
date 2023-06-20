import os
import pygame
from main import mainmenu

def charactercreator():
    pygame.init()

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Character Creator")

    image_filename = "characterbackground.png"
    image_path = os.path.join("gameimages", image_filename)
    background_image = pygame.image.load(image_path)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 600 <= mouse_pos[0] <= 650 and 10 <= mouse_pos[1] <= 30:
                    running = False
                    mainmenu()

        screen.blit(background_image, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), (600, 10, 50, 20))

        font = pygame.font.Font(None, 18)
        back_text = font.render("Back", True, (255, 255, 255))
        screen.blit(back_text, (605, 12))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    charactercreator()
