import pygame
import mainmenu
import charactercreator

def mainmenu():
    pygame.init()

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Horse Game")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                mainmenu.mainmenu()

        pygame.display.flip()

    pygame.quit()
    exit()

if __name__ == "__main__":
    mainmenu()
