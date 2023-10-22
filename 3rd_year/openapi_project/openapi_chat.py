import flet as ft
import openai
openai.api_key = "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 wew"


def main(page : ft.Page):
    page.scroll=True
    page.theme_mode = "light"

    def btn_clicked(e):
        
        # completion = openai.ChatCompletion.create(
        #         model="gpt-3.5-turbo", 
        #         messages=[
        #             {"role": "system", "content": "You are useful assistant"},
        #             {"role": "user", "content": str(text_input)},
        #         ]
        #     )
        # output = completion.choices[0].message.content
        
        clear_button = ft.FloatingActionButton("Clear", height=60, on_click=clear)
        page.add(clear_button)
        page.add(ft.Container(ft.Text(value=text_input.value), bgcolor=ft.colors.BLUE_GREY_100, padding=10))
        page.add(ft.Container(ft.Text(value="output", selectable=True), padding=10))
        text_input.value = ""
        page.update()

    #heading
    heading = ft.Text(value="ChatGPT Chatbot", size=24)
    # create a text input field
    text_input = ft.TextField(hint_text="Enter your prompt", expand=True, multiline=True)
    # create a submit button
    submit_button = ft.ElevatedButton("Submit", height=60, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=1)), on_click=btn_clicked)
    # place everything you want in one row into the row object in a list
    row = ft.Row([text_input, submit_button])
    page.add(heading, row)
 
    def clear(e):
        if page.controls == 1:
            pass
        else:
            page.controls.pop()                        
            page.update()

    
ft.app(target=main)