import flet as ft


class Task(ft.Column): # Task component

    def __init__(self, task_name, task_status_change, task_delete): # Initialize the task component
        super().__init__()
        self.completed = False
        self.task_name = task_name
        self.task_status_change = task_status_change
        self.task_delete = task_delete
        self.display_task = ft.Checkbox(value=False, label=self.task_name, on_change=self.status_changed)
        self.edit_name = ft.TextField(expand=1)

        self.display_view = ft.Row( 
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

    def status_changed(self, e): # Function to handle status change
        self.completed = self.display_task.value
        self.task_status_change()

    def delete_clicked(self, e): # Function to delete the task
        self.task_delete(self)

class TodoApp(ft.Column): # Main To-Do App component
    def __init__(self):
        super().__init__()
        self.new_task = ft.TextField(hint_text="Create a new task...", expand=True)
        self.tasks = ft.Column()

        self.filter = ft.Tabs( # Tabs for filtering tasks
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[ft.Tab(text="All"), ft.Tab(text="Active"), ft.Tab(text="Completed")],
        )

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
            ft.Column(
                spacing=25,
                controls=[
                    self.filter,
                    self.tasks,
                ]
            )
        ]

    def add_clicked(self, e): # Function to add a new task
        task = Task(self.new_task.value, self.task_status_change, self.task_delete)
        self.tasks.controls.append(task)
        self.new_task.value = ""
        self.update()

    def task_status_change(self): # Function to update task status
        self.update()

    def task_delete(self, task): # Function to delete a task
        self.tasks.controls.remove(task)
        self.update()

    def before_update(self): # Function to filter tasks before updating the UI
        status = self.filter.tabs[self.filter.selected_index].text
        for task in self.tasks.controls:
            task.visible = (
                status == "All"
                or (status == "Active" and not task.completed)
                or (status == "Completed" and task.completed)
            )

    def tabs_changed(self, e): # Function to handle tab changes
        self.update()

def main(page: ft.Page):
    page.title = "To-Do App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    # create an app instance
    todo = TodoApp()

    page.add(todo) # add the app controls to the page

ft.app(target=main)