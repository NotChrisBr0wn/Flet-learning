import flet as ft

class Task(ft.Column): # Task component

    def __init__(self, task_name, task_delete): # Initialize the task with its name and delete function
        super().__init__()
        self.task_name = task_name
        self.task_delete = task_delete
        self.display_task = ft.Checkbox(value=False, label=self.task_name)
        self.edit_name = ft.TextField(expand=1)

        self.display.view = ft.Row( 
             alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
             vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    self.display_task,
                    ft.Row( 
                         spacing = 0,
                         controls = [
                              ft.IconButton(
                                icon=ft.Icons.CREATE_OUTLINED,
                                tooltip="Edit task",
                                on_click=self.edited_clicked,
                              ),
                              ft.IconButton(
                                icon=ft.Icons.DELETE_OUTLINE,
                                tooltip="Delete task",
                                on_click=self.delete_clicked,
                              ),
                         ],
                    ),
                ],
        )

        self.edit_view = ft.Row(
             visible = False,
             alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
             vertical_alignment=ft.CrossAxisAlignment.CENTER,
             controls=[
                 self.edit_name,
                 ft.IconButton(
                    icon=ft.Icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.Colors.GREEN,
                    tooltip="Save changes",
                    on_click=self.save_clicked,
                ),
            ],
        )
        self.controls = [self.display_view, self.edit_view] 
    
    def edited_clicked(self, e): # Function to switch to edit mode
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()
    
    def save_clicked(self, e): # Function to save the edited task name
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def delete_clicked(self, e): # Function to delete the task
        self.task_delete(self)
    
class TodoApp(ft.Column): # Main To-Do App component
    def __init__(self):
        super().__init__()
        self.new_task = ft.TextField(hint_text="Create a new task...", expand=True)
        self.tasks = ft.Column()
        self.width = 600
        self.controls = [ # Adds a plus button and the new task input field
            ft.Row(
                controls=[
                    self.new_task,
                    ft.FloatingActionButton(
                        icon=ft.Icons.ADD, on_click=self.add_clicked
                    ),
                ],
            ),
            self.tasks,
        ]

    def add_clicked(self, e): # Function to add a new task
        task = Task(self.new_task.value, self.task_delete)
        self.tasks.controls.append(task)
        self.new_task.value = ""
        self.update()

    def task_delete(self, task): # Function to delete a task
        self.tasks.controls.remove(task)
        self.update()

def main(page: ft.Page):
    page.title = "To-Do App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    # create an app instance
    todo = TodoApp()

    page.add(todo) # add the app controls to the page

ft.app(target=main)