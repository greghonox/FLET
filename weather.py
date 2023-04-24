import flet
from flet import *
import datetime
from random import randint, choice


APIKEY = '439ebe1275fbb228903479a2b39bf403'

days = [
    'Domingo',
    'Segunda',
    'Terca',
    'Quarta',
    'Quinta',
    'Sexta',
    'Sabado'
]

def get_ico_weather():
    weather_icons = ['sol', 'chuva', 'nublado']
    return choice(weather_icons)

def _current_extra():
    _extra_info = []
    _extra = [[
        randint(1, 100) / 1000,
        'Km',
        'Visibility',
        './assets/por_sol.png'
        ],[
        randint(1, 100) * .43,
        'Km',
        'Pressure',
        './assets/lua.png'
    ],[
        randint(1, 100) * .43,
        'Km',
        'Pressure',
        './assets/views.png'
    ],[
        randint(1, 100) * .43,
        'Km',
        'Pressure',
        './assets/barometro.png'
    ]]
    for info in _extra:
        _extra_info.append(
            Container(
                bgcolor='white10',
                border_radius=12,
                alignment=alignment.center,
                content=Column(
                    alignment='center',
                    horizontal_alignment='center',
                    spacing=25,
                    controls=[
                        Container(
                            alignment=alignment.center,
                            content=Image(
                                src=info[3],
                                color='white',
                            ),
                            width=32,
                            height=32
                        ),
                        Container(
                            content=Column(
                                alignment=alignment.center,
                                horizontal_alignment=alignment.center,
                                spacing=0,
                                controls=[
                                    Text(
                                        f'{info[0]} {info[1]}'
                                    )
                                ]
                            )
                        )
                    ]
                )
            )
        )
    return _extra_info
    
def _get_weather(lat=33.44, lon=94.04, part='hourly,daily'):
    directions = ['north', 'south', 'west', 'east']
    return {'temperature': randint(-20, 50),
            'wind': randint(20, 100),
            'humidity': randint(20, 50),
            'thermo': randint(20, 80),
            'direction': choice(directions)}

def main(page: Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    
    def _expand(e):
        _c.content.controls[1].height = 560 if e.data == 'true' else 660 * .4
        _c.content.controls[1].update()
            
    def _top():
        _today = _get_weather()
        gradient = LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.top_right,
                colors=['lightblue600', 'lightblue900']
        )
        _today_extra = GridView(
            max_extent=150,
            expand=1,
            run_spacing=5,
            spacing=5
        )
        for info in _current_extra():
            _today_extra.controls.append(info)
            
        top = Container(
            width=310,
            height=660 * .4,
            gradient=gradient,
            border_radius=35,
            animate=animation.Animation(
                duration=350,
                curve='decelerate',
            ),
            on_hover=lambda e: _expand(e),
            padding=15,
            content=Column(
                alignment='start',
                spacing=10,
                controls=[
                    Row(
                        alignment='center',
                        controls=[
                            Text('Hortolandia/Brasil',
                                size=16,
                                width='w500')
                        ]),
                    Container(padding=padding.only(bottom=5)),
                    Row(
                        alignment='center',
                        spacing=30,
                        controls=[
                            Column(
                                controls=[
                                    Container(
                                        width=90,
                                        height=90,
                                        image_src="./assets/ico.png"
                                    )
                                ]
                            ),
                            Column(
                                spacing=5,
                                horizontal_alignment='center',
                                controls=[
                                    Text(
                                        'Hoje',
                                         size=12,
                                         text_align='center'
                                    ),
                                    Text(
                                        f'{datetime.datetime.now().strftime("%d/%m/%Y")}',
                                         size=10,
                                         text_align='center',
                                         color='white30'
                                    ),
                                    Row(
                                        vertical_alignment='start',
                                        spacing=0,
                                        controls=[
                                            Container(
                                                content=Text(
                                                    _today['temperature'],
                                                    size=32,
                                                    text_align='center'
                                                )
                                            ),
                                            Container(
                                                content=Text(
                                                    'º',
                                                    size=32,
                                                    text_align='center'
                                                )
                                            )                                            
                                        ]
                                    ),
                                    Text(
                                        str(_today['direction']) + ' - Overcast',
                                        size=10,
                                        color='white10',
                                        text_align='center'
                                    )
                                ]
                            ),
                            
                        ]
                    ),
                            Divider(
                                height=8,
                                thickness=1,
                                color='white10',
                            ),
                            Row(
                                alignment='spaceAround',
                                controls=[
                                    Container(
                                        content=Column(
                                            horizontal_alignment='center',
                                            spacing=2,
                                            controls=[
                                                Container(
                                                    alignment=alignment.center,
                                                    content=Image(src='./assets/wind.png', color='white'),                                                    
                                                    width=20,
                                                    height=20,
                                                ),
                                                Text(
                                                    str(_today['wind']) + ' km/h',
                                                    size=11
                                                ),
                                                Text(
                                                    'Vento',
                                                    size=8,
                                                    color='white30'
                                                )
                                            ]
                                        )
                                    ),
                                    Container(
                                        content=Column(
                                            horizontal_alignment='center',
                                            spacing=2,
                                            controls=[
                                                Container(
                                                    alignment=alignment.center,
                                                    content=Image(src='./assets/humidity.png', color='white'),                                                    
                                                    width=20,
                                                    height=20,
                                                ),
                                                Text(
                                                    str(_today['humidity']) + '%',
                                                    size=11
                                                ),
                                                Text(
                                                    'Humidade',
                                                    size=8,
                                                    color='white30'
                                                )
                                            ]
                                        )
                                    ),
                                    Container(
                                        content=Column(
                                            horizontal_alignment='center',
                                            spacing=2,
                                            controls=[
                                                Container(
                                                    alignment=alignment.center,
                                                    content=Image(src='./assets/termometro.png', color='white'),                                                    
                                                    width=20,
                                                    height=20,
                                                ),
                                                Text(
                                                    str(_today['thermo']) + 'º',
                                                    size=11
                                                ),
                                                Text(
                                                    'Termometro',
                                                    size=8,
                                                    color='white30'
                                                )
                                            ]
                                        )
                                    )  
                                ]
                            ),
                            _today_extra
                ]
            )
        )
        return top

    def _botton_data():
        _botton_data = []        
        for day in days:
            _botton_data.append(
                Row(
                    spacing=5,
                    alignment='spaceBetween',
                    controls=[
                        Row(
                            expand=1,
                            alignment='start',
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    content=Text(
                                        day
                                    )
                                )
                            ]                            
                        ),
                        Row(
                            expand=1,
                            controls=[
                                Container(
                                    content=Row(
                                        alignment='start',
                                        controls=[
                                            Container(
                                                width=20, height=20,
                                                alignment=alignment.center_left,
                                                content=Image(src=f'./assets/{get_ico_weather()}.png')
                                            )
                                        ]
                                    )
                                )
                            ]
                        ),
                        Text(
                            f'{randint(-20, 6)}º  {randint(-20, 6)}º'
                        )
                    ]
                )
            )
        return _botton_data

    def _botton():
        _bot_column = Column(
            alignment='center',
            horizontal_alignment='center',
            spacing=25
        )
        for data in _botton_data():
            _bot_column.controls.append(data)            
            
        _bottom = Container(
            padding=padding.only(top=280, left=20, right=20, bottom=20),
            content=_bot_column
        )
        return _bottom
        
        
    stack = Stack(
            width=300, height=550,
            controls=[
                _botton(),
                _top(),
            ]
    )
    _c = Container(
        width=310,
        height=660,
        bgcolor='black',
        padding=10,
        border_radius=35,
        content=stack
    )
    page.window_title_bar_hidden = True
    page.window_bgcolor = colors.TRANSPARENT
    page.bgcolor = colors.TRANSPARENT    
    page.window_frameless = True

    page.add(_c)
    
if '__main__' ==  __name__:
    flet.app(target=main, assets_dir='assets')