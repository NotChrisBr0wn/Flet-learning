import flet as ft

class CalcButton(ft.ElevatedButton): # class for calculator buttons
    def __init__(self,text, expand = 1):
        super().__init__()
        self.text = text
        self.expand = expand
        
class DigitButton(CalcButton): # class for digit button
    def __init__(self,text, expand = 1):
        CalcButton.__init__(self,text, expand)
        self.bgcolor = ft.Colors.WHITE24
        self.color = ft.Colors.WHITE
        
class ActionButton(CalcButton): # class for action button
    def __init__(self,text):
        CalcButton.__init__(self,text)
        self.bgcolor = ft.Colors.ORANGE
        self.color = ft.Colors.WHITE
        
class ExtraActionButton(CalcButton): # class for extra action button
    def __init__(self,text):
        CalcButton.__init__(self,text)
        self.bgcolor = ft.Colors.BLUE_GREY_100
        self.color = ft.Colors.BLACK

class CalculatorApp(ft.Container):
    def __init__(self):
        super().__init__()
        
        self.result = ft.Text(value="0", color=ft.Colors.WHITE, size=20)
        self.width = 350
        self.bgcolor = ft.Colors.BLACK
        self.border_radius = ft.border_radius.all(20)
        self.padding = 20
        self.content = ft.Column(
            controls=[
                ft.Row(controls=[self.result], alignment="end"),
                ft.Row(
                    controls=[
                        ExtraActionButton(text="AC"),
                        ExtraActionButton(text="+/-"),
                        ExtraActionButton(text="%"),
                        ActionButton(text="/"),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(text="7"),
                        DigitButton(text="8"),
                        DigitButton(text="9"),
                        ActionButton(text="*"),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(text="4"),
                        DigitButton(text="5"),
                        DigitButton(text="6"),
                        ActionButton(text="-"),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(text="1"),
                        DigitButton(text="2"),
                        DigitButton(text="3"),
                        ActionButton(text="+"),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(text="0", expand=2),
                        DigitButton(text="."),
                        ActionButton(text="="),
                    ]
                ),
            ]
        )

def main(page: ft.Page):
   page.title = "Calculator App"
   calc = CakculatorApp()
   page.add(calc)
    
ft.app(main)