import pygame
import os
from PIL import Image

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Horse Game")

def main_menu():
    # Load and display the background image
    image_filename = "mainbackground.png"
    image_path = os.path.join("gameimages", image_filename)
    background_image = pygame.image.load(image_path).convert()
    screen.blit(background_image, (0, 0))

    # Create a button for the new game
    new_game_button = pygame.Rect(100, 200, 200, 50)

    # Main menu loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if new_game_button.collidepoint(mouse_pos):
                        cutscene()
                        character_creator()

        # Draw the buttons
        pygame.draw.rect(screen, (255, 0, 0), new_game_button)

        # Update the screen
        pygame.display.flip()

def cutscene():
    # Add your code for the cutscene here
    print("Cutscene...")
    # Rest of the code for the cutscene

def character_creator():
    # Add your code for the character creator here
    print("Character creator...")
    # Rest of the code for the character creator

# Entry point of the program
if __name__ == "__main__":
    main_menu()
