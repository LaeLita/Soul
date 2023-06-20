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

    # Create menu option buttons
    new_game_button_rect = pygame.Rect(100, 200, 200, 50)
    load_game_button_rect = pygame.Rect(100, 300, 200, 50)
    settings_button_rect = pygame.Rect(100, 400, 200, 50)
    exit_game_button_rect = pygame.Rect(100, 500, 200, 50)

    # Main menu loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if new_game_button_rect.collidepoint(mouse_pos):
                    charactercreator()
                elif load_game_button_rect.collidepoint(mouse_pos):
                    load_game()
                elif settings_button_rect.collidepoint(mouse_pos):
                    settings()
                elif exit_game_button_rect.collidepoint(mouse_pos):
                    exit_game()

        # Draw the background image on the screen
        screen.blit(background_image, (0, 0))

        # Draw the menu options
        pygame.draw.rect(screen, (255, 0, 0), new_game_button_rect)
        pygame.draw.rect(screen, (0, 255, 0), load_game_button_rect)
        pygame.draw.rect(screen, (0, 0, 255), settings_button_rect)
        pygame.draw.rect(screen, (255, 255, 0), exit_game_button_rect)

        pygame.display.flip()

    # Clean up and exit the game
    pygame.quit()
    exit()

def new_game():
    # Add your code for starting a new game here
    print("Starting a new game...")
    # Rest of the code for the new game

def load_game():
    # Add your code for loading a game here
    print("Loading a game...")
    # Rest of the code for loading the game

def settings():
    # Add your code for the settings menu here
    print("Settings menu...")
    # Rest of the code for the settings menu

def exit_game():
    print("Exiting the game...")
    # Add any necessary cleanup code here
    # Exiting the program
    exit()

# Entry point of the program
if __name__ == "__main__":
    main_menu()
