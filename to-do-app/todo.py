import flet as ft

class TodoApp(ft.Column): # The app root controll is the column containing all the controls

    def __init__(self):
        super().__init__()
        self.new_task = ft.TextField(hint_text="What needs to be done?", expand=True) # Adds a text field for new tasks
        self.tasks_view = ft.Column()
        self.width = 600,
        self.controls = [
            ft.Row(
                controls=[
                    self.new_task,
                    ft.FloatingActionButton(
                        icon=ft.Icons.ADD, on_click =self.add_clicked
                    ),
                ],
            ),
            self.tasks_view,
        ]
        
    def add_clicked(self,e): # Adds a new task to the list
            self.tasks_view.controls.append(ft.Checkbox(label=self.new_task.value))
            self.new_task.value = ""
            self.view.update()

def main(page: ft.Page):
    page.title = "To-Do App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(TodoApp())

    # create an app instance
    todo = TodoApp()
    page.add(todo) # add the app controls to the page
ft.app(main)