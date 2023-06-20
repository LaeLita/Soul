import os
import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Horse Game")

def main_menu():
    # Load the background image
    image_filename = "mainbackground.png"
    image_path = os.path.join("gameimages", image_filename)
    background_image = pygame.image.load(image_path).convert()

    # Main menu loop
    running = True
    while running:
        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the background image
        screen.blit(background_image, (0, 0))

        # Draw the menu options
        menu_font = pygame.font.Font(None, 32)
        text = menu_font.render("===== Horse Game =====", True, (255, 255, 255))
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, 50))

        menu_options = ["1. New Game", "2. Load Game", "3. Settings", "4. Exit Game"]
        for i, option in enumerate(menu_options):
            text = menu_font.render(option, True, (255, 255, 255))
            screen.blit(text, (screen_width // 2 - text.get_width() // 2, 150 + i * 50))

        # Update the display
        pygame.display.flip()

        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    new_game()
                elif event.key == pygame.K_2:
                    load_game()
                elif event.key == pygame.K_3:
                    settings()
                elif event.key == pygame.K_4:
                    exit_game()

    # Clean up
    pygame.quit()

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
    pygame.quit()
    exit()

# Entry point of the program
if __name__ == "__main__":
    main_menu()
