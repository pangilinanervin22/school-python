import flet as ft
import googletrans
import asyncio

from flet import (
    Dropdown,
    TextButton,
    TextField,
    Page,
    Stack
)

list_of_languages = []
for key, value in googletrans.LANGUAGES.items():
    list_of_languages.append(ft.dropdown.Option(value))

translator = googletrans.Translator()


def main(page: Page):
    page.title = "Flet translator example"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.theme_mode = "light"
    page.scrollable = True
    page.window_width = 720

    # Event handlers
    def text_changed(e):
        outputTextTranslate.value = f"{inputTextTranslate.value}"
        page.update()

    def dropdown_changed(e):
        print(languageDropDown.value)
        page.update()

    def button_clicked(e):
        if inputTextTranslate.value == "":
            print("No text to translate")
            return
        output = translator.translate(
            inputTextTranslate.value, dest=languageDropDown.value)
        outputTextTranslate.value = f"Output: {output.text}"
        print(output.text)
        page.update()

    # UI components
    inputTextTranslate = TextField(
        label='Text to translate:', on_change=text_changed, value="Ako ay isang mabuting tao")
    outputTextTranslate = ft.Text("")
    languageDropDown = Dropdown(on_change=dropdown_changed,
                                options=list_of_languages, value="english")
    buttonTranslate = TextButton(text='Translate', icon_color='red',
                                 icon='translate', on_click=button_clicked,)

    page.add(
        ft.Row(controls=(inputTextTranslate, languageDropDown),
               alignment='center',),
        buttonTranslate,
        outputTextTranslate,
    )


ft.app(target=main)
