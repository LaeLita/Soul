import os
import pygame
from main_menu import main_menu

def charactercreator():
    # Initialize Pygame
    pygame.init()

    # Set up the Pygame window
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Character Creator")

    # Load the character creator background image
    image_filename = "charactercreator.png"
    image_path = os.path.join("gameimages", image_filename)
    background_image = pygame.image.load(image_path)

    # Character creator loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    if is_back_clicked(event.pos):
                        running = False
                        main_menu()  # Return to the main menu

        # Draw the background image on the screen
        screen.blit(background_image, (0, 0))

        # Draw character creator elements
        # ... (code for drawing character creator elements goes here)

        pygame.display.flip()

    # Clean up and exit the character creator
    pygame.quit()
    exit()

def is_back_clicked(mouse_pos):
    # Add your logic here to determine if the "Back" button is clicked
    # based on the mouse position
    return True  # Replace with your actual logic

# Entry point of the character creator
if __name__ == "__main__":
    character_creator()
