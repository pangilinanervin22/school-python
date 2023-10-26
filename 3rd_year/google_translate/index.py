import flet as ft
import googletrans

list_of_languages = []
for key, value in googletrans.LANGUAGES.items():
    list_of_languages.append(ft.dropdown.Option(value))

translator = googletrans.Translator()


def main(page: ft.Page):
    page.title = "Flet translator example"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.theme_mode = "light"
    page.scrollable = True
    page.window_width = 720

    # Event handlers
    def text_changed(e):
        output = translator.translate(
            inputTextTranslate.value, dest=languageDropDown.value)
        outputTextTranslate.value = f"Output: {output.text}"
        print(output.text)
        page.update()

    def dropdown_changed(e):
        output = translator.translate(
            inputTextTranslate.value, dest=languageDropDown.value)
        outputTextTranslate.value = f"Output: {output.text}"
        print(output.text)
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
    inputTextTranslate = ft.TextField(
        label='Text to translate:', on_change=text_changed, value="Ako ay isang mabuting tao")
    outputTextTranslate = ft.Text(
        bgcolor="red", color="white", size=20, selectable=True)
    languageDropDown = ft.Dropdown(on_change=dropdown_changed,
                                   options=list_of_languages, value="english")
    buttonTranslate = ft.OutlinedButton(
        text='Translate', on_click=button_clicked, icon="translate")

    page.add(
        ft.Row(controls=(inputTextTranslate, languageDropDown),
               alignment='center',),
        buttonTranslate,
        outputTextTranslate,
    )


ft.app(target=main)
