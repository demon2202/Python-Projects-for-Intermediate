import tkinter as tk
import random

def get_computer_choice():
    """Generate computer's choice"""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner"""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(user_choice):
    """Play the game with user's choice"""
    # Reset labels
    user_choice_label.config(text=f"You chose: {user_choice.capitalize()}")
    computer_choice_label.config(text="Computer chose: ")
    result_label.config(text="")
    
    # Animate computer's choice
    animate_computer_choice(user_choice)

def animate_computer_choice(user_choice):
    """Animate computer's choice"""
    choices = ['rock', 'paper', 'scissors']
    current_index = 0
    
    def update_choice():
        nonlocal current_index
        computer_choice_label.config(text=f"Computer chose: {choices[current_index].capitalize()}")
        current_index = (current_index + 1) % len(choices)
        if current_index == 0:
            # When animation completes, get the actual computer's choice and determine the winner
            computer_choice = get_computer_choice()
            computer_choice_label.config(text=f"Computer chose: {computer_choice.capitalize()}")
            result = determine_winner(user_choice, computer_choice)
            result_label.config(text=result)
        else:
            # Continue animating
            computer_choice_label.after(200, update_choice)
    
    # Start animation
    update_choice()

# Create main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# Create widgets
instruction_label = tk.Label(root, text="Choose your move:")
rock_button = tk.Button(root, text="Rock", width=10, command=lambda: play_game('rock'))
paper_button = tk.Button(root, text="Paper", width=10, command=lambda: play_game('paper'))
scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: play_game('scissors'))
user_choice_label = tk.Label(root, text="")
computer_choice_label = tk.Label(root, text="")
result_label = tk.Label(root, text="")

# Layout widgets using grid
instruction_label.grid(row=0, column=0, columnspan=3, pady=10)
rock_button.grid(row=1, column=0, padx=10)
paper_button.grid(row=1, column=1, padx=10)
scissors_button.grid(row=1, column=2, padx=10)
user_choice_label.grid(row=2, column=0, columnspan=3)
computer_choice_label.grid(row=3, column=0, columnspan=3)
result_label.grid(row=4, column=0, columnspan=3, pady=10)

# Start the GUI
root.mainloop()
