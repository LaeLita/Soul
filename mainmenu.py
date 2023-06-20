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
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if new_game_button_rect.collidepoint(mouse_pos):
                    character_creator()

        # Draw the background image on the screen
        screen.blit(background_image, (0, 0))

        # Draw the menu options
        new_game_button_rect = pygame.Rect(100, 200, 200, 50)
        pygame.draw.rect(screen, (0, 255, 0), new_game_button_rect)

        pygame.display.flip()

    # Clean up and exit the game
    pygame.quit()
    exit()

def character_creator():
    # Add your code for the character creator here
    print("Character Creator")

# Entry point of the program
if __name__ == "__main__":
    main_menu()
