import flet as ft
import qrcode

image_qr = ft.Image(
    src=f"wew.png",
    width=240,
    height=240,
    fit=ft.ImageFit.CONTAIN,
)


def main(page: ft.Page):
    page.title = "Flet translator example"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.theme_mode = "light"
    page.window_width = 720

    # Event handlers

    def sample_click(e):
        # project_qrcode.makeSomething()
        print("start")

        # qr = pyqrcode.create("https://www.youtube.com")
        # qr.png("wew.png", scale=8)

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        # Add the text to the QR code
        qr.add_data("wew")
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color="black", back_color="white")
        qr_image.save("wew.png")

        page.add(image_qr)
        page.update()

    # Ui components
    input_text = ft.TextField(
        label='Link:', value="https://www.youtube.com/")

    button_generate = ft.TextButton(
        text='Generate', icon_color='red', icon=ft.icons.CREATE_NEW_FOLDER, on_click=sample_click)

    page.add(input_text, button_generate)


ft.app(target=main)
