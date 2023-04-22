import flet as ft

def main(page: ft.Page):
    t = ft.Text(value='Jesus esta voltando', color='yellow')
    page.controls.append(t)
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER, port=5000)