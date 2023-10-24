from flet import (Text, TextField, ElevatedButton, Row,
                  Container, colors, ButtonStyle, FloatingActionButton, RoundedRectangleBorder, app)
import flet as ft
import openai
openai.api_key = "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"


def main(page: ft.Page):
    page.scroll = True
    page.theme_mode = "light"

    def btn_clicked(e):

        # completion = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo",
        #     messages=[
        #         {"role": "system", "content": "You are useful assistant"},
        #         {"role": "user", "content": str(text_input)},
        #     ]
        # )
        # output = completion.choices[0].message.content

        clear_button = FloatingActionButton(
            "Clear", height=60, on_click=clear)
        page.add(clear_button)
        page.add(Container(Text(value=text_input.value),
                 bgcolor=colors.BLUE_GREY_100, padding=10))
        page.add(Container(
            Text(value="dssdsds", selectable=True), padding=10))
        text_input.value = ""
        page.update()

    heading = Text(value="ChatGPT Chatbot", size=24)
    text_input = TextField(
        hint_text="Enter your prompt", expand=True, multiline=True)
    submit_button = ElevatedButton("Submit", height=60, style=ButtonStyle(
        shape=RoundedRectangleBorder(radius=1)), on_click=btn_clicked)
    row = Row([text_input, submit_button])
    page.add(heading, row)

    def clear(e):
        if page.controls == 1:
            pass
        else:
            page.controls.pop()
            page.update()
            page.controls.pop()
            page.update()


app(target=main)
