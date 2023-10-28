import flet as ft
import googletrans
import openai
openai.api_key = ""


# Iterate the googletrans list of languages and make array of options
list_languages = []
for key, value in googletrans.LANGUAGES.items():
    list_languages.append(ft.dropdown.Option(value))

# Googletrans Chatbot integration


def translate_text(text, language):
    translator = googletrans.Translator()
    output = translator.translate(
        text, dest=language)

    text = f"Output: {output.text}"
    return output.text


def main(page: ft.Page):
    page.scroll = True
    page.theme_mode = "light"

    # Event handler for button click
    def btn_clicked(e):

        # OpenAI Chatbot integration
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": str(text_input.value)},
            ]
        )

        # Get the output of OpenAI chatbot
        ouput_openai = completion.choices[0].message.content
        # Translate the output of OpenAI chatbot
        translate_openai = translate_text(ouput_openai, languageDropDown.value)
        # Add the input and output to the page
        page.add(ft.Container(ft.Text(value=text_input.value),
                 bgcolor=ft.colors.BLUE_GREY_100, padding=10))
        page.add(ft.Container(
            ft.Text(value=f"({languageDropDown.value}): {translate_openai}", selectable=True), padding=10))

        # Clear the input field
        text_input.value = ""
        page.update()

    # Event handler for clear button
    def click_clear(e):
        if len(page.controls) == 4:
            return
        else:
            # for clearing the last 2 messages
            page.controls.pop()
            page.controls.pop()
            page.update()

    # UI components
    title_heading = ft.Text(
        value="ChatGPT Chatbot Translating Output", size=24)
    languageDropDown = ft.Dropdown(width=250,
                                   options=list_languages, value="filipino")

    text_input = ft.TextField(
        hint_text="Enter your prompt", expand=True, multiline=True)

    submit_button = ft.ElevatedButton(
        "Submit", height=60,  on_click=btn_clicked)

    input_row = ft.Row([text_input, submit_button])

    clear_button = ft.FloatingActionButton(
        "Clear", height=60, on_click=click_clear)

    # Add components to page
    page.add(title_heading, languageDropDown, input_row, clear_button)


ft.app(target=main)
