import flet as ft


def main(page: ft.Page):
    def add_clicked(e): # Adds a new task to the list
        tasks_view.controls.append(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        view.update()

    new_task = ft.TextField(hint_text="What needs to be done?", expand=True) # Adds a text field for new tasks
    tasks_view = ft.Column()
    view=ft.Column( # Main page layout
        width=600,
        controls=[
            ft.Row(
                controls=[
                    new_task,
                    ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_clicked),
                ],
            ),
            tasks_view,
        ],
    )

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER # Centers all the content horizontally
    page.add(view)

ft.app(main)