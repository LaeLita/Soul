import os
import pygame

def main_menu():
    # Initialize Pygame
    pygame.init()

    # Set up the Pygame window
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Horse Game")

    # Load the background image
    image_filename = "mainbackground.png"
    image_path = os.path.join("gameimages", image_filename)
    background_image = pygame.image.load(image_path)

    # Main menu loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw the background image on the screen
        screen.blit(background_image, (0, 0))

        # Draw the menu options
        # ... (code for drawing menu options goes here)

        pygame.display.flip()

    # Clean up and exit the game
    pygame.quit()
    exit()

# Entry point of the program
if __name__ == "__main__":
    main_menu()
