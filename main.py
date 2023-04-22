import flet as ft


def main(page: ft.Page):
    
    first_name = ft.TextField(label='First Name', autofocus=True)
    last_name = ft.TextField(label='Last Name')
    greeting = ft.Column()
    
    def button_clicked(e):
        greeting.controls.append(
            ft.Text(f'Hello {first_name.value} {last_name.value}!')
        )
        first_name.value = ''
        last_name.value = ''
        page.update()
        first_name.focus()
        
        
    page.add(
        first_name,
        last_name,
        ft.ElevatedButton('Click', on_click=button_clicked),
        greeting
    )
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER, port=5000)