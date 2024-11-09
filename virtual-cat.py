
class Cat:  # Define a class named Cat to represent a virtual cat
    def __init__(self, name):  # Initialize the Cat object with a name and attributes
        self.name = name  # Set the cat's name from user input
        self.energy = self.stomach = 2  # Initialize both energy and stomach capacity to 2

    def play(self):  # Define a method to play with the cat
        if self.energy > 0:  # Check if the cat has energy left to play
            print(f"{self.name} says meow")  # Print a message indicating the cat is playing
            self.energy -= 1  # Decrease energy by 1 each time the cat plays
        else:
            print(f"{self.name} is tired")  # Print a message if the cat is out of energy

    def eat(self):  # Define a method to feed the cat
        if self.stomach > 0:  # Check if the cat has room left to eat
            print(f"{self.name} says nom")  # Print a message indicating the cat is eating
            self.stomach -= 1  # Decrease stomach capacity by 1 each time the cat eats
        else:
            print(f"{self.name} is full")  # Print a message if the cat is full

def main():  # Define the main function to run the program
    cat = Cat(input("Enter a name for your cat: "))  # Ask the user for a cat name and create a Cat object

    # Start a loop that continues until the user enters 'n'
    while input("Interact with the cat (play/feed) or 'n' to exit: ").lower() != 'n':
        action = input("Choose action (play/feed): ").strip().lower()  # Ask the user to choose an action
        if action == 'play':  # If user chooses 'play'
            cat.play()  # Call the play method on the cat
        elif action == 'feed':  # If user chooses 'feed'
            cat.eat()  # Call the eat method on the cat
        else:
            print("Invalid option. Please enter 'play' or 'feed'.")  # Handle invalid input

if __name__ == "__main__":  # Check if this script is being run directly
    main()  # Call the main function to start the program
