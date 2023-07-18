from tkinter import *
from data import question_data

THEME_COLOR = "#375362"


class QuizzInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score
        self.score = Label(text="Score: 0", bg=THEME_COLOR, foreground="white", font=("Arial", 16, "italic"))
        self.score.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(width=300, height=250)
        self.canvas.create_text(150, 125, text=f"{question_data[0]['question']}", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # True Button
        true_image = PhotoImage(file="images/true.png")
        self.button = Button(image=true_image, highlightthickness=0)
        self.button.grid(row=2, column=0)

        # False Button
        false_image = PhotoImage(file="images/false.png")
        self.button = Button(image=false_image, highlightthickness=0)
        self.button.grid(row=2, column=1)



        self.window.mainloop()