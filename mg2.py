import tkinter as tk
from tkinter import messagebox

class MastermindGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Mastermind Game")
        
        self.create_widgets()
        
        self.reset_game()

    def create_widgets(self):
        self.info_label = tk.Label(self.root, text="Player 1: Enter a number")
        self.info_label.pack()
        
        self.entry = tk.Entry(self.root, show="*")
        self.entry.pack()
        
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_number)
        self.submit_button.pack()
        
        self.guess_label = tk.Label(self.root, text="")
        self.guess_label.pack()
        
        self.guess_entry = tk.Entry(self.root)
        self.guess_entry.pack()
        
        self.guess_button = tk.Button(self.root, text="Guess", command=self.make_guess)
        self.guess_button.pack()
        
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()
        
    def reset_game(self):
        self.player1_number = ""
        self.player2_number = ""
        self.player1_attempts = 0
        self.player2_attempts = 0
        self.current_player = 1
        self.guess_entry.config(state='disabled')
        self.guess_button.config(state='disabled')
        self.info_label.config(text="Player 1: Enter a number")
        self.entry.config(show="*")
        self.entry.delete(0, tk.END)
        self.guess_label.config(text="")
        self.result_label.config(text="")
    
    def submit_number(self):
        number = self.entry.get()
        if not number.isdigit():
            messagebox.showerror("Error", "Please enter a valid number")
            return
        
        if self.current_player == 1:
            self.player1_number = number
            self.info_label.config(text="Player 2: Guess the number")
        else:
            self.player2_number = number
            self.info_label.config(text="Player 1: Guess the number")
        
        self.entry.delete(0, tk.END)
        self.entry.config(state='disabled')
        self.submit_button.config(state='disabled')
        self.guess_entry.config(state='normal')
        self.guess_button.config(state='normal')
    
    def make_guess(self):
        guess = self.guess_entry.get()
        if not guess.isdigit():
            messagebox.showerror("Error", "Please enter a valid number")
            return
        
        if self.current_player == 1:
            correct_number = self.player1_number
            self.player2_attempts += 1
        else:
            correct_number = self.player2_number    
            self.player1_attempts += 1
            
        if guess == correct_number:
            if self.current_player == 1:
                self.result_label.config(text=f"Player 2 guessed correctly in {self.player2_attempts} attempts")
                self.current_player = 2
                self.prepare_next_round("Player 2: Enter a number")
            else:
                self.result_label.config(text=f"Player 1 guessed correctly in {self.player1_attempts} attempts")
                self.declare_winner()
            return
        
        correct_digits = sum(1 for a, b in zip(guess, correct_number) if a == b)
        self.guess_label.config(text=f"Correct digits in correct place: {correct_digits}")
        self.guess_entry.delete(0, tk.END)
    
    def prepare_next_round(self, info_text):
        self.entry.config(state='normal', show="*")
        self.submit_button.config(state='normal')
        self.guess_entry.config(state='disabled')
        self.guess_button.config(state='disabled')
        self.info_label.config(text=info_text)
    
    def declare_winner(self):
        if self.player1_attempts < self.player2_attempts:
            winner_message = "Player 1 wins and is crowned Mastermind!"
        else:
            winner_message = "Player 2 wins and is crowned Mastermind!"
        messagebox.showinfo("Game Over", winner_message)
        self.reset_game()

root = tk.Tk()
game = MastermindGame(root)
root.mainloop()
