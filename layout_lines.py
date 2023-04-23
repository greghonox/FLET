import flet as ft


def main(page: ft.Page):
    def items(count):
        items = []
        for cc in range(1, count + 1):
            items.append(
                ft.Container(
                    content=ft.Text(value=str(cc)),
                    alignment=ft.alignment.center,
                    width=50,
                    height=50,
                    bgcolor=ft.colors.AMBER,
                    border_radius=ft.border_radius.all(5)
                )
            )
        return items
    
    def gap_slider_change_horizontal(e):
        row.spacing = int(e.control.value)
        row.update()

    def gap_slider_change_vertical(e):
        cols.spacing = int(e.control.value)
        cols.update()
                
    gap_slider_horizontal = ft.Slider(
        min=0,
        max=50,
        divisions=50,
        value=0,
        label='{value}',
        on_change=gap_slider_change_horizontal
    )
    gap_slider_vertical = ft.Slider(
        min=0,
        max=50,
        divisions=50,
        value=0,
        label='{value}',
        on_change=gap_slider_change_vertical
    )    
    row = ft.Row(spacing=0, controls=items(10))
    cols = ft.Column(spacing=0, controls=items(10))
    
    def slider_change(e):
        row_last.width = float(e.control.value)
        row_last.update()
        
    width_slider = ft.Slider(
        min=0,
        max=page.window_width,
        divisions=50,
        value=page.window_width,
        label="{value}",
        on_change=slider_change,
    )

    row_last = ft.Row(
        wrap=True,
        spacing=10,
        run_spacing=10,
        controls=items(30),
        width=page.window_width,
    )
        
    page.auto_scroll = True   
    page.add(ft.Column([ft.Text('Espaco entre items'), gap_slider_horizontal, 
             row, gap_slider_vertical, cols]), width_slider, row_last)
    
    
ft.app(target=main, view=ft.WEB_BROWSER)