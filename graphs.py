import  flet as ft
import time 
from random import uniform

COLS = 50
GOLD = [(n, uniform(1, 20)) for n in range(COLS)]
SILVER = [(n, uniform(1, 20)) for n in range(COLS)]


class TimeChart(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.data_points: list = []
        self.points: list = GOLD
        
        self.chart: ft.Control = ft.LineChart(
            tooltip_bgcolor=ft.colors.with_opacity(.75, ft.colors.WHITE),
            expand=True,
            min_y= (int(min(self.points, key=lambda y: y[1])[1], )),
            max_y= (int(max(self.points, key=lambda y: y[1])[1], )),           
            min_x= (int(min(self.points, key=lambda x: x[0])[0], )),
            max_x= (int(max(self.points, key=lambda x: x[0])[0], )),
            left_axis=ft.ChartAxis(labels_size=50),
            bottom_axis=ft.ChartAxis(labels_size=40, labels_interval=1)
        )
        self.lin_chart: ft.Control = ft.LineChartData(
            color=ft.colors.RED,
            stroke_width=2,
            curved=True,
            stroke_cap_round=True,
            below_line_gradient=ft.LinearGradient(
                                        begin=ft.alignment.top_center,
                                        end=ft.alignment.bottom_center,
                                        colors=[ft.colors.with_opacity(0.25, ft.colors.GREEN),
                                                'transparent']
                                                  )
        )
        
    def create_data_points(self, x, y):
        return ft.LineChartDataPoint(
            x, y, selected_below_line=ft.ChartPointLine(
                width=.5, color="white54", dash_pattern=[2, 4]
            ),
            selected_point=ft.ChartCirclePoint(stroke_width=1)
        )
        
    def get_data_points(self):
        for x, y in self.points:
            self.data_points.append(self.create_data_points(x, y))
            self.chart.update()
            time.sleep(.5)
                
    def build(self):
        self.lin_chart.data_points = self.data_points
        self.chart.data_series = [self.lin_chart]
        return ft.Column(
            horizontal_alignment='center',
            controls=[
                ft.Text('Historico em formato de grafico',
                    size=16,
                    weight='bold'
                ),
                self.chart
            ]
        )

    def toggle_data(self, e):
        self.switch_list(e)
        self.chart.data_series = [self.lin_chart]
        self.get_data_points()
        
    def switch_list(self, e):
        self.points = GOLD if e.control.data == 'gold' else SILVER
        self.data_points = []
        self.chart.data_series = []
        self.lin_chart.data_points = self.data_points
        self.chart.min_y= (int(min(self.points, key=lambda y: y[1])[1], )),
        self.chart.max_y= (int(max(self.points, key=lambda y: y[1])[1], )),           
        self.chart.min_x= (int(min(self.points, key=lambda x: x[0])[0], )),
        self.chart.max_x= (int(max(self.points, key=lambda x: x[0])[0], )),
        self.chart.update()
        time.sleep(.5)

    def get_data_buttons(self, btn_name, data):
        return ft.ElevatedButton(
            btn_name,
            color='white',
            height=40,
            width=140,
            style=ft.ButtonStyle(
                shape={"": ft.RoundedRectangleBorder(radius=6)}
            ),
            bgcolor='teal600',
            data=data,
            on_click=lambda e: self.toggle_data(e),
        )
    
    
def main(page: ft.Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    chart = TimeChart()    
    column_main = ft.Column(
        expand=True,
        alignment='center',
        horizontal_alignment='center',
        controls=[ft.Container(
            expand=True,
            border_radius=6,
            bgcolor=ft.colors.with_opacity(.025, ft.colors.WHITE10),
            content=ft.Row(
                alignment='center', 
                controls=[
                    chart.get_data_buttons('Bitcoin', 'bitcoin'),
                    chart.get_data_buttons('Gold', 'gold'),
                ]
            )
        ),
            ft.Container(
                expand=4,
                border_radius=6,
                bgcolor=ft.colors.with_opacity(.025, ft.colors.WHITE10),
                content=chart,
                padding=20,
            )
            ]
    )
    
    page.add(
        column_main
    )
    page.update()
    chart.get_data_points()
    
    
if __name__ == '__main__':
    ft.app(target=main)