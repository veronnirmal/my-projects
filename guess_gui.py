import tkinter as tk
from tkinter import messagebox

class GuessMyNumberGame:
    def __init__(self, master):
        self.master = master
        master.title("Guess My Number ")
        master.geometry("700x500")

        self.low = 1
        self.high = 100
        self.attempts = 0

        self.label = tk.Label(master, text="Think of a number between 1 and 100", font=("Arial", 12))
        self.label.pack(pady=20)

        self.guess_label = tk.Label(master, text="", font=("Arial", 16, "bold"))
        self.guess_label.pack(pady=10)

        self.guess_button = tk.Button(master, text="Start Guessing", command=self.make_guess)
        self.guess_button.pack(pady=10)

        self.buttons_frame = tk.Frame(master)
        self.buttons_frame.pack()

        self.low_button = tk.Button(self.buttons_frame, text="Too Low", command=self.too_low, state='disabled')
        self.low_button.grid(row=0, column=0, padx=10)

        self.high_button = tk.Button(self.buttons_frame, text="Too High", command=self.too_high, state='disabled')
        self.high_button.grid(row=0, column=1, padx=10)

        self.correct_button = tk.Button(self.buttons_frame, text="Correct", command=self.correct, state='disabled')
        self.correct_button.grid(row=0, column=2, padx=10)

    def make_guess(self):
        if self.low > self.high:
            messagebox.showerror("Oops!", "There seems to be an inconsistency in your feedback.")
            return
        self.guess = (self.low + self.high) // 2
        self.attempts += 1
        self.guess_label.config(text=f"My guess is: {self.guess}")
        self.low_button.config(state='normal')
        self.high_button.config(state='normal')
        self.correct_button.config(state='normal')
        self.guess_button.config(state='disabled')

    def too_low(self):
        self.low = self.guess + 1
        self.next_guess()

    def too_high(self):
        self.high = self.guess - 1
        self.next_guess()

    def correct(self):
        messagebox.showinfo("Victory!", f"I guessed your number {self.guess} in {self.attempts} attempts!")
        self.reset_game()

    def next_guess(self):
        self.guess_button.config(state='normal')
        self.low_button.config(state='disabled')
        self.high_button.config(state='disabled')
        self.correct_button.config(state='disabled')
        self.guess_label.config(text="Click 'Start Guessing' for the next guess")

    def reset_game(self):
        self.low = 1
        self.high = 100
        self.attempts = 0
        self.guess_label.config(text="")
        self.guess_button.config(state='normal')
        self.low_button.config(state='disabled')
        self.high_button.config(state='disabled')
        self.correct_button.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessMyNumberGame(root)
    root.mainloop()
