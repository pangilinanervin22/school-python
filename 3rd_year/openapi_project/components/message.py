class CounterParams(ft.UserControl):
    def __init__(self, initial_count):
        super().__init__()
        self.counter = initial_count

    def build(self):
        text = ft.Text(str(self.counter))
        def add_click(e):
            self.counter += 1
            text.value = str(self.counter)
            self.update()

        return ft.Row([text, ft.ElevatedButton("Add", on_click=add_click)])