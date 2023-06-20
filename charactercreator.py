import os
import pygame
from main import main_menu

def character_creator():
    # Initialize Pygame
    pygame.init()

    # Set up the Pygame window
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Character Creator")

    # Load the background image
    image_filename = "characterbackground.png"
    image_path = os.path.join("gameimages", image_filename)
    background_image = pygame.image.load(image_path)

    # Create "Back" button
    back_button_rect = pygame.Rect(650, 50, 100, 50)

    # Character creator loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if back_button_rect.collidepoint(mouse_pos):
                    running = False
                    main_menu()

        # Draw the background image on the screen
        screen.blit(background_image, (0, 0))

        # Draw the "Back" button
        pygame.draw.rect(screen, (255, 0, 0), back_button_rect)
        font = pygame.font.Font(None, 36)
        text = font.render("Back", True, (255, 255, 255))
        screen.blit(text, (660, 60))

        pygame.display.flip()

    # Clean up and exit the character creator
    pygame.quit()
    exit()

# Entry point of the program
if __name__ == "__main__":
    character_creator()
