import flet as ft
import ListQuestion as lq
import Demo


def main(page: ft.Page):
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.window_width = "500"
    page.window_height = "700"
    page.theme_mode = "light"

    main_container = ft.Container(
        content=ft.Column([ft.Text("Hello World!"),
                           ft.Text("Hello World!"),
                           ft.Text("Hello World!")]),
        bgcolor=ft.colors.PINK_100,
        padding=5,
        width="400px"
    )

    #

    page.add(main_container)
    page.add(Demo.QuizApp())


ft.app(target=main)
