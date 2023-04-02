import customtkinter as CTk
from PIL import Image


class QuizApp(CTk.CTk):
    """Класс приложения-викторины, наследующий функционал главного окна tkinter"""

    def __init__(self):
        super().__init__()

        self.width, self.height = 800, 600
        self.geometry(f"{self.width}x{self.height}")  # Задаем размеры окна
        self.title("Викторина")
        self.resizable(False, False)

        self.logo = CTk.CTkImage(
            dark_image=Image.open("Images/Logo.png"), size=(289, 49)
        )
        self.logo_label = CTk.CTkLabel(
            master=self, text="", image=self.logo, width=self.width, height=100
        )
        self.logo_label.grid(row=0, column=0)

        self.init_main_frame()
        self.init_quiz_frame()

    def init_main_frame(self):
        """Создаем главный фрейм с кнопками управления"""
        self.main_frame = CTk.CTkFrame(master=self, fg_color="black")
        self.main_frame.grid(
            row=1, column=0, padx=(20, 20), pady=(100, 100), sticky="NSEW"
        )
        self.main_frame.grid_anchor(
            "center"  # Вырваниваем все элементы внутри фрейма по центру
        )

        self.start_button = CTk.CTkButton(
            master=self.main_frame, text="Начать", command=self.start_quiz
        )
        self.start_button.grid(row=0, column=0, pady=(30, 30))

        self.setting_button = CTk.CTkButton(
            master=self.main_frame, text="Настройки", command=self.open_setting
        )
        self.setting_button.grid(row=1, column=0, pady=(30, 30))

        self.exit_button = CTk.CTkButton(
            master=self.main_frame, text="Выход", command=self.destroy
        )
        self.exit_button.grid(row=2, column=0, pady=(30, 30))

    def init_quiz_frame(self):
        """Создаем фрейм викторины с вопросом и кнопками выбора ответа"""
        self.quize_frame = CTk.CTkFrame(master=self, fg_color="transparent")
        self.quize_frame.grid(row=1, column=0, padx=(20, 20), sticky="NSEW")
        self.quize_frame.grid_anchor(
            "center"  # Вырваниваем все элементы внутри фрейма по центру
        )
        self.quize_frame.grid_forget()

        self.question_label = CTk.CTkLabel(
            master=self.quize_frame, text="Ваш вопрос", font=(CTk.CTkFont(size=20))
        )
        self.question_label.grid(row=0, column=0)

        self.question_image = CTk.CTkImage(
            dark_image=Image.open("Images/QuestionsImage/1.gif"), size=(100, 100)
        )
        self.question_image = CTk.CTkLabel(
            master=self.quize_frame,
            text="",
            image=self.question_image,
            width=self.width,
            height=150,
        )
        self.question_image.grid_forget()

        self.answers_frame = CTk.CTkFrame(
            master=self.quize_frame, fg_color="transparent"
        )
        self.answers_frame.grid(
            row=2, column=0, padx=(20, 20), pady=(20, 20), sticky="NSEW"
        )
        self.answers_frame.grid_anchor(
            "center"  # Вырваниваем все элементы внутри фрейма по центру
        )

        self.answer_1_button = CTk.CTkButton(
            master=self.answers_frame,
            text="Вариант 1 ............................................",
            command=lambda: self.check_answer(self.answer_1_button.cget("text")),
            font=(CTk.CTkFont(size=16)),
        )
        self.answer_1_button.grid(row=0, column=0, padx=(20, 20), pady=(20, 20))

        self.answer_2_button = CTk.CTkButton(
            master=self.answers_frame,
            text="Вариант 2",
            command=lambda: self.check_answer(self.answer_2_button.cget("text")),
            font=(CTk.CTkFont(size=16)),
        )
        self.answer_2_button.grid(row=0, column=1, padx=(20, 20), pady=(20, 20))

        self.answer_3_button = CTk.CTkButton(
            master=self.answers_frame,
            text="Вариант 3",
            command=lambda: self.check_answer(self.answer_3_button.cget("text")),
            font=(CTk.CTkFont(size=16)),
        )
        self.answer_3_button.grid(row=1, column=0, padx=(20, 20), pady=(20, 20))

        self.answer_4_button = CTk.CTkButton(
            master=self.answers_frame,
            text="Вариант 4",
            command=lambda: self.check_answer(self.answer_4_button.cget("text")),
            font=(CTk.CTkFont(size=16)),
        )
        self.answer_4_button.grid(row=1, column=1, padx=(20, 20), pady=(20, 20))

        self.exit_to_main_button = CTk.CTkButton(
            master=self.quize_frame,
            text="Выйти в меню",
            command=self.open_main,
            fg_color="black",
        )
        self.exit_to_main_button.grid(row=3, column=0, pady=(40, 0))

    def start_quiz(self):
        self.main_frame.grid_forget()
        self.quize_frame.grid(row=1, column=0)

    def check_answer(self, text):
        print(text)

    def open_main(self):
        self.main_frame.grid(row=1, column=0)
        self.quize_frame.grid_forget()

    def open_setting(self):
        pass


if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
