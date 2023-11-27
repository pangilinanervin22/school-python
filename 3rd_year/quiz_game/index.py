import flet as ft
import ListQuestion

#  SINGLETON FOR GLOBAL VARIABLE
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance._value = 0  # Initial value
        return cls._instance

    @property
    def value(self):
        return self._value

    def set_value(self, new_value):
        self._value = new_value


user_score = Singleton()
class QuizApp(ft.UserControl,):
    def list_question(self, questions):
        list = []

        for question in questions:
            list.append(ft.Text(question))
        return list

    def build(self):
        user_score.set_value(0)
        self.listOfQuestion = ListQuestion.get_random_question(10)
        self.position = 0
        self.points = 0
        question_text = ft.Text(f"Question: {self.position + 1}\n{self.listOfQuestion[self.position]['question']} ",size=20,weight=ft.FontWeight.W_700)
        choices = ft.Column(controls=self.list_question(
            self.listOfQuestion[self.position]["choices"]))
        input_text = ft.TextField()

        # print all questions
        print("All Questions")
        for question in self.listOfQuestion:
            print(question["question"])

        def submit_answer(e: ft.TapEvent):
            # check if answer is correct
            input_text.error_text = None
            self.update()
            current = self.listOfQuestion[self.position]
            if input_text.value == "":
                input_text.error_text = "please input a letter"
                self.update()
                return
            elif str.upper(input_text.value) == current["answer"]:

                self.points += 1
                print("Correct!")
            else:
                print("Wrong!")

            # block if end of quiz
            if (self.position == len(self.listOfQuestion) - 1):

                user_score.set_value(self.points)
                print(user_score.value)
                print("End of Quiz total points: " + str(self.points) + " out of " + str(len(self.listOfQuestion)))
                self.page.go("/score")
                return

                # change question
            self.position += 1
            current = self.listOfQuestion[self.position]
            question_text.value = f"Question: {self.position + 1}\n{current['question']}"
            choices.controls = self.list_question(current["choices"])
            input_text.value = ""
            self.update()

        return ft.Column([question_text, choices, input_text, ft.ElevatedButton("Submit", on_click=submit_answer,width=500,height=40,bgcolor="blue",color="white")])


def main(page: ft.Page):
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.window_width = "500"
    page.window_height = "700"
    page.theme_mode = "light"
    page.padding = 0
    page.margin = 0


    main_container = ft.Container(
        content=ft.Column([QuizApp()]),
        padding=100,
        width=1000,

    )
    user_score_text = ft.Text("")
    page.update()
    quiz_view = ft.View("/quiz",
                        [
                            ft.AppBar(title=ft.Text("Quiz Time!"), bgcolor=ft.colors.SURFACE_VARIANT),
                            main_container,
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        )

    score_view = ft.View("/score",[user_score_text,ft.ElevatedButton("Try Again",on_click= lambda _: page.go("/quiz"),width=300,height=40,bgcolor="blue",color="white") ]
                         ,horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    def route_change(route):
        user_score_text.value = f" your score is: {user_score.value}/10"
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Group 1: Quiz App"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.Container(
                        ft.Text("CodeMinds Challenge", text_align="center", size=40, weight=ft.FontWeight.W_900),
                         padding=100
                    ),
                    ft.ElevatedButton("Start", on_click=lambda _: page.go("/quiz"), color="white", bgcolor="blue",width=120,  # Set the width of the button
    height=50),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,

            )
        )
        # add routes here:
        if page.route == "/quiz":
            page.views.append(
                quiz_view
            )
        elif page.route == "/score":
            page.views.append(score_view)
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)




ft.app(target=main)