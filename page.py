from time import sleep
import flet as ft

def main(page: ft.Page):
    def click(e):
        page.splash = ft.ProgressBar(bgcolor='red')
        page.update()
        sleep(5)
        page.splash = None
        page.update()
    
    page.title = "My awesome app"
    # page.window_bgcolor = ft.colors.TRANSPARENT # Define transparencia para os componentes da janela
    # page.bgcolor = ft.colors.TRANSPARENT  # Define transparencia para os componentes da janela
    page.window_title_bar_hidden = True
    page.window_frameless = True
    page.window_left = 400
    page.window_top = 200
    # page.window_skip_task_bar = True # Ocuta icone da barra
    page.add(ft.ElevatedButton("I'm a floating button!", on_click=click))
    page.add(ft.ElevatedButton('close app', on_click=lambda e: page.window_destroy()))
    
ft.app(target=main)