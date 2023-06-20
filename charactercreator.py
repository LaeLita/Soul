import pygame
import os

def charactercreator():
    pygame.init()

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Character Creator")

    background_color = (255, 255, 255)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 650 <= mouse_pos[0] <= 780 and 10 <= mouse_pos[1] <= 40:
                    running = False

        screen.fill(background_color)
        pygame.draw.rect(screen, (0, 0, 0), (650, 10, 130, 30))
        font = pygame.font.Font(None, 24)
        back_text = font.render("Back", True, (255, 255, 255))
        screen.blit(back_text, (670, 15))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    charactercreator()
