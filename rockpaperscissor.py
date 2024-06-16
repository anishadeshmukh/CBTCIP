import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")
        
        self.setup_ui()
    
    def setup_ui(self):
        self.info_label = tk.Label(self.root, text="Select Rock, Paper, or Scissors:")
        self.info_label.pack()
        
        self.rock_button = tk.Button(self.root, text="Rock", command=lambda: self.player_selection("Rock"))
        self.rock_button.pack(side=tk.LEFT, padx=10)
        
        self.paper_button = tk.Button(self.root, text="Paper", command=lambda: self.player_selection("Paper"))
        self.paper_button.pack(side=tk.LEFT, padx=10)
        
        self.scissors_button = tk.Button(self.root, text="Scissors", command=lambda: self.player_selection("Scissors"))
        self.scissors_button.pack(side=tk.LEFT, padx=10)
        
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=20)
    
    def player_selection(self, player_choice):
        options = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(options)
        
        outcome = self.get_result(player_choice, computer_choice)
        
        self.result_label.config(text=f"Player chose: {player_choice}\nComputer chose: {computer_choice}\nOutcome: {outcome}")
    
    def get_result(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "It's a tie!"
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            return "Player wins!"
        else:
            return "Computer wins!"

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
