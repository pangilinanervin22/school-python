import flet as ft

def main(page: ft.Page):
    # page.vertical_alignment = "center"
    # page.horizontal_alignment = "center"
    page.window_width = "500"
    page.window_height = "700"
    page.theme_mode = "light"

    number_text = ft.Text(0)
    
    def add_click(e):
        number_text.value = str(int(number_text.value) + 1)
        page.update()
        print(number_text.value)

    chat_message = ft.Container([
            number_text, 
            ft.ElevatedButton("Add", on_click=add_click, )
        ],)
    
    page.add(chat_message)
    
    chat_message.controls.append(ft.Text("Hello"))
    page.update()
    
    
    
      
ft.app(target=main)