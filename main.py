import customtkinter as CTk
from PIL import Image


class QuizApp(CTk.CTk):
    """Класс приложения-викторины, наследующий функционал главного окна tkinter"""

    def __init__(self):
        super().__init__()

        self.geometry("800x500")  # Размеры окна


if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()


print("dawd")
listed = [1, 2, 3, 3, 4, 4, 4, 4, 4, 4]
