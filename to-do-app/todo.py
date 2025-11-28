import flet as ft

def main(page: ft.Page):
    def add_clicked(e):
        page.add(ft.checkbox(label="new_task.value"))
        new_task.value = ""
        page.update()
    
    new_task = ft.TextField(hint_text="Create a new task...")

    page.add(new_task, ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_clicked))

ft.app(main)