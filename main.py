import customtkinter as CTk
from PIL import Image
from questions import QuestProcess


class QuizApp(CTk.CTk):
    """Класс приложения-викторины, наследующий функционал главного окна tkinter"""

    def __init__(self):
        super().__init__()

        self.current_quiz_name = None
        self.old_answer_button = None
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

        self.answer_buttons = []

        self.init_questions_json()
        self.init_result_frame()
        self.init_main_frame()
        self.init_select_quiz_frame()
        self.init_quiz_frame()

    def init_main_frame(self):
        """Создаем главный фрейм с кнопками управления"""
        self.main_frame = CTk.CTkFrame(master=self, fg_color="transparent")
        self.main_frame.grid(
            row=1, column=0, padx=(20, 20), pady=(100, 100), sticky="NSEW"
        )
        self.main_frame.grid_anchor(
            "center"  # Вырваниваем все элементы внутри фрейма по центру
        )

        self.start_button = CTk.CTkButton(
            master=self.main_frame,
            text="Начать",
            command=self.open_select_quiz,  # old: self.start_quiz
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
        self.question_image_label = CTk.CTkLabel(
            master=self.quize_frame,
            text="",
            image=self.question_image,
            width=self.width,
            height=150,
        )
        self.question_image_label.grid_forget()

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
            text="Вариант 1",
            command=lambda: self.select_answer(
                self.answer_1_button.cget("text"), self.answer_1_button
            ),
            font=(CTk.CTkFont(size=16)),
        )
        self.answer_1_button.grid(row=0, column=0, padx=(20, 20), pady=(20, 20))

        self.answer_2_button = CTk.CTkButton(
            master=self.answers_frame,
            text="Вариант 2",
            command=lambda: self.select_answer(
                self.answer_2_button.cget("text"), self.answer_2_button
            ),
            font=(CTk.CTkFont(size=16)),
        )
        self.answer_2_button.grid(row=0, column=1, padx=(20, 20), pady=(20, 20))

        self.answer_3_button = CTk.CTkButton(
            master=self.answers_frame,
            text="Вариант 3",
            command=lambda: self.select_answer(
                self.answer_3_button.cget("text"), self.answer_3_button
            ),
            font=(CTk.CTkFont(size=16)),
        )
        self.answer_3_button.grid(row=1, column=0, padx=(20, 20), pady=(20, 20))

        self.answer_4_button = CTk.CTkButton(
            master=self.answers_frame,
            text="Вариант 4",
            command=lambda: self.select_answer(
                self.answer_4_button.cget("text"), self.answer_4_button
            ),
            font=(CTk.CTkFont(size=16)),
        )
        self.answer_4_button.grid(row=1, column=1, padx=(20, 20), pady=(20, 20))

        self.answer_buttons = [
            self.answer_1_button,
            self.answer_2_button,
            self.answer_3_button,
            self.answer_4_button,
        ]

        self.next_button = CTk.CTkButton(
            master=self.quize_frame,
            text="Дальше",
            command=self.to_next_question,
            fg_color="gray",
        )
        self.next_button.grid(row=3, column=0, pady=(20, 0))

        self.exit_to_main_button = CTk.CTkButton(
            master=self.quize_frame,
            text="Выйти в меню",
            command=self.open_main,
            fg_color="black",
        )
        self.exit_to_main_button.grid(row=4, column=0, pady=(40, 0))

        # self.set_quest_and_answer()

    def init_select_quiz_frame(self):
        """Создаем фрейм викторины с вопросом и кнопками выбора ответа"""
        self.select_quize_frame = CTk.CTkFrame(master=self, fg_color="transparent")
        self.select_quize_frame.grid(row=1, column=0, padx=(20, 20), sticky="NSEW")
        self.select_quize_frame.grid_anchor(
            "center"  # Вырваниваем все элементы внутри фрейма по центру
        )
        self.select_quize_frame.grid_forget()

        quizes = self.quest_processor.load_list_quiz()
        select_button = []
        for i in range(len(quizes)):
            select_button.append(
                CTk.CTkButton(master=self.select_quize_frame, text=quizes[i])
            )
            select_button[i].configure(
                command=lambda x=select_button[i]: self.start_quiz(x)
            )
            select_button[i].grid(row=i, column=0, pady=(20, 20))

    def init_questions_json(self):
        self.quest_processor = QuestProcess()

    def set_quest_and_answer(self):
        if self.quest_processor.can_get_question():
            self.quest_processor.selected_answer = None
            quest, options, answer, image = self.quest_processor.get_question()
            self.question_label.configure(text=quest)
            self.answer_1_button.configure(text=options[0])
            self.answer_2_button.configure(text=options[1])
            self.answer_3_button.configure(text=options[2])
            self.answer_4_button.configure(text=options[3])
            if image:
                self.question_image_label.grid(row=1, column=0)
            else:
                self.question_image_label.grid_forget()

        else:
            self.open_result()
            print("Не могу выдать вопрос")
            pass
            # ToDo: Создать фрейм вывода результатов
            # self.question_label.configure(text="Вопросы закончились!")

    def to_next_question(self):
        """Вызывается next_button, переход к ледующему вопросу и проверка ответа текущего"""
        if self.quest_processor.selected_answer:
            self.quest_processor.check_answer()
            self.set_quest_and_answer()
            self.reset_color_answer_buttons()
        elif not self.quest_processor.can_get_question():
            self.open_result()
        else:
            pass

    def reset_color_answer_buttons(self):
        for button in self.answer_buttons:
            button.configure(fg_color=("#3B8ED0", "#1F6AA5"))

    def start_quiz(self, name_quiz):
        print(name_quiz.cget("text"))
        self.select_quize_frame.grid_forget()
        self.quize_frame.grid(row=1, column=0, padx=(20, 20), sticky="NSEW")
        self.current_quiz_name = name_quiz.cget("text")
        self.quest_processor.load_quiz(self.current_quiz_name)
        self.set_quest_and_answer()

    def select_answer(self, text, button):
        if self.old_answer_button:
            self.old_answer_button.configure(fg_color=("#3B8ED0", "#1F6AA5"))
        button.configure(fg_color="green")
        print(text)
        self.old_answer_button = button
        self.quest_processor.selected_answer = text

    def open_main(self):
        self.main_frame.grid(
            row=1, column=0, padx=(20, 20), pady=(100, 100), sticky="NSEW"
        )
        self.quize_frame.grid_forget()
        self.result_frame.grid_forget()
        self.quest_processor.reset_quiz()

    def open_setting(self):
        pass

    def open_select_quiz(self):
        self.main_frame.grid_forget()
        self.select_quize_frame.grid(row=1, column=0)

    def init_result_frame(self):
        """Создаем фрейм результатов"""
        self.result_frame = CTk.CTkFrame(master=self, fg_color="transparent")
        self.result_frame.grid(row=1, column=0, padx=(20, 20), sticky="NSEW")
        self.result_frame.grid_anchor(
            "center"  # Вырваниваем все элементы внутри фрейма по центру
        )
        self.result_frame.grid_forget()

        self.result_label = CTk.CTkLabel(
            master=self.result_frame,
            text=f"Ваш результат:{self.quest_processor.statistics[0]} из {sum(self.quest_processor.statistics)}",
            font=(CTk.CTkFont(size=20)),
        )
        self.result_label.grid(row=0, column=0)

        self.exit_to_main_button = CTk.CTkButton(
            master=self.result_frame,
            text="Выйти в меню",
            command=self.open_main,
            fg_color="black",
        )
        self.exit_to_main_button.grid(row=4, column=0, pady=(40, 0))

    def open_result(self):
        self.quize_frame.grid_forget()
        self.result_label.configure(
            text=f"Ваш результат:{self.quest_processor.statistics[0]} из {sum(self.quest_processor.statistics)}"
        )
        self.result_frame.grid(row=1, column=0)


if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
