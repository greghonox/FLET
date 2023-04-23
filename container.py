import flet as ft

def main(page: ft.Page):
    page.title = 'Container background'

    def animate_container(e):
        c1.width = 100 if c1.width == 200 else 200
        c1.height = 100 if c1.height == 200 else 200
        c1.bgcolor = "blue" if c1.bgcolor == ft.colors.YELLOW else ft.colors.YELLOW
        c1.update()    
            
    c1 = ft.Container(
        content=ft.ElevatedButton("Elevated Button in Container"),
        bgcolor=ft.colors.YELLOW,
        padding=5,
        on_click=animate_container,
        animate=ft.animation.Animation(1000, "bounceOut"),
    )

    c2 = ft.Container(
        content=ft.ElevatedButton(
            "Elevated Button with opacity=0.5 in Container", opacity=0.5
        ),
        bgcolor=ft.colors.YELLOW,
        padding=5,
    )

    c3 = ft.Container(
        content=ft.OutlinedButton("Outlined Button in Container"),
        bgcolor=ft.colors.YELLOW,
        padding=5,
    )
    columns_buttons = ft.Row(
        [
            ft.Container(
                content=ft.Text("Non clickable"),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.AMBER,
                width=150,
                height=150,
                border_radius=10,
            ),
            ft.Container(
                content=ft.Text("Clickable without Ink"),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.GREEN_200,
                width=150,
                height=150,
                border_radius=10,
                on_click=lambda e: print("Clickable without Ink clicked!"),
            ),
            ft.Container(
                content=ft.Text("Clickable with Ink"),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.CYAN_200,
                width=150,
                height=150,
                border_radius=10,
                ink=True,
                on_click=lambda e: print("Clickable with Ink clicked!"),
            ),
            ft.Container(
                content=ft.Text("Clickable transparent with Ink"),
                margin=10,
                padding=10,
                alignment=ft.alignment.center,
                width=150,
                height=150,
                border_radius=10,
                ink=True,
                on_click=lambda e: print("Clickable transparent with Ink clicked!"),
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER, # Esse que centraliza esse botao
        )
            
    page.add(c1, c2, c3, columns_buttons)
    
    
ft.app(target=main)