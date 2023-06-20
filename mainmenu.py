import os
import pygame
from charactercreator import charactercreator

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
    show_menu = True
    while show_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                show_menu = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    if is_new_game_clicked(event.pos):
                        show_menu = False
                        character_creator()  # Open the character creator

        # Draw the background image on the screen
        screen.blit(background_image, (0, 0))

        # Draw the menu options
        # ... (code for drawing menu options goes here)

        pygame.display.flip()

    # Clean up and exit the game
    pygame.quit()
    exit()

def is_new_game_clicked(mouse_pos):
    # Add your logic here to determine if the "New Game" button is clicked
    # based on the mouse position
    return True  # Replace with your actual logic

# Entry point of the program
if __name__ == "__main__":
    main_menu()
