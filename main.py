import flet as ft


def main(page: ft.Page):
    
    def button_clicked(e):
        print(f'click {e}')
        page.add(ft.Text("Clicked!", size=100))
        page.update()
        
    page.add(
        ft.Row(
            controls=[
                ft.Text(f'A {x}') for x in range(10)
            ] + [ft.ElevatedButton(text="Say my name!", on_click=button_clicked)]
        )
    )
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER, port=5000)