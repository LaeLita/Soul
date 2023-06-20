import mainmenu
import pygame

def mainmenu():
    # Your code for the main menu goes here
    # ...

    pygame.event.wait()  # Wait for any key press

    pygame.quit()
    mainmenu.main_menu()  # Call the main_menu() function from mainmenu.py

if __name__ == "__main__":
    mainmenu()


