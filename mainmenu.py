import os
from PIL import Image

def main_menu():
    # Load and display the background image
    image_filename = "mainbackground.png"
    image_path = os.path.join("gameimages", image_filename)
    background_image = Image.open(image_path)
    background_image.show()

    print("===== Horse Game =====")
    print("1. New Game")
    print("2. Load Game")
    print("3. Settings")
    print("4. Exit Game")

    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        new_game()
    elif choice == "2":
        load_game()
    elif choice == "3":
        settings()
    elif choice == "4":
        exit_game()
    else:
        print("Invalid choice. Please try again.")
        main_menu()

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