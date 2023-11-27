import flet as ft
import ListQuestion

class QuizApp(ft.UserControl):
    def list_question(self, questions):
        list = []

        for question in questions:
            list.append(ft.Text(question))
        return list

    def build(self):
        self.listOfQuestion = ListQuestion.get_random_question(9)
        self.position = 0
        self.points = 0
        question_text = ft.Text(f"Question: {self.position + 1}\n{self.listOfQuestion[self.position]['question']} ")
        choices = ft.Column(controls=self.list_question(
            self.listOfQuestion[self.position]["choices"]))
        input_text = ft.TextField()
        
        # print all questions
        print("All Questions")
        for question in self.listOfQuestion:
            print(question["question"])
            
        def submit_answer(e: ft.TapEvent):
            # check if answer is correct
            current = self.listOfQuestion[self.position]
            if str.upper(input_text.value) == current["answer"]:
                self.points += 1
                print("Correct!")
            else:
                print("Wrong!")
            
            # block if end of quiz
            if(self.position == len(self.listOfQuestion) - 1):
                print("End of Quiz total points: " + str(self.points) + " out of " + str(len(self.listOfQuestion)))
                return 
            
            # change question
            self.position += 1
            current = self.listOfQuestion[self.position]
            question_text.value = current["question"]
            choices.controls = self.list_question(current["choices"])
            input_text.value = ""
            self.update()

        return ft.Column([question_text, choices, input_text, ft.ElevatedButton("Submit", on_click=submit_answer)])


def main(page: ft.Page):
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.window_width = "500"
    page.window_height = "700"
    page.theme_mode = "light"

    main_container = ft.Container(
        content=ft.Column([QuizApp()]),
        bgcolor=ft.colors.PINK_100,
        padding=5,
        width="400px"
    )

    #

    page.add(main_container)


ft.app(target=main)