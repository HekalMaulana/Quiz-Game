from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizzInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score
        self.score = Label(text="Score: 0", bg=THEME_COLOR, foreground="white", font=("Arial", 16, "italic"))
        self.score.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question",
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # True Button
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_button)
        self.true_button.grid(row=2, column=0)

        # False Button
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_button)
        self.false_button.grid(row=2, column=1)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,
                                   text=question
                                   )
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(
                                    self.question_text,
                                    text=f"Congrats you complete the quiz."
                                    )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_button(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_button(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        self.window.after(1000, self.next_question)
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

