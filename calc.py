from flet import app, Container, colors, Row, Column, Page, Text, ElevatedButton


def definition_button(text: str, color: colors=colors.BLACK, 
                      bgcolor: colors=colors.BLUE_GREY_100, expand=1) -> ElevatedButton:
    return ElevatedButton(
        text=text,
        data=text,        
        bgcolor=bgcolor,
        color=color,
        expand=expand,
    )

def main(page: Page) -> None:
    page.title = 'My Calc Flet'
    page.theme_mode = 'dark'
    page.window_width = 300

    result = Text(value='0') 
    
    page.add(
        Container(
            width=300,   
            content=Column(
                alignment='center',
                controls=[
                        Row(controls=[result]),
                        Row(controls=[
                            definition_button(
                                "AC",
                                colors.BLUE_GREY_100,
                                colors.BLACK,
                            ),
                            definition_button(
                                '+/-',
                                colors.BLUE_GREY_100,
                                colors.BLACK,
                            ),
                            definition_button(
                                '%',
                                colors.BLUE_GREY_100,
                                colors.BLACK,
                            ),
                            definition_button(
                                '/',
                                colors.BLUE_GREY_100,
                                colors.RED,
                            ),
                        ]
                        ),
                        Row(controls=[
                            definition_button('7'),
                            definition_button('8'),
                            definition_button('9'),
                            definition_button(
                                '*',
                                colors.BLUE_GREY_100,
                                colors.RED,
                            ),
                        ]
                        ),
                        Row(controls=[
                            definition_button('4'),
                            definition_button('5'),
                            definition_button('6'),
                            definition_button(
                                '-',
                                colors.BLUE_GREY_100,
                                colors.RED,
                            ),
                        ]
                        ),
                        Row(controls=[
                            definition_button('1'),
                            definition_button('2'),
                            definition_button('3'),
                            definition_button(
                                '+',
                                colors.BLUE_GREY_100,
                                colors.RED,
                            ),
                        ]
                        ),        
                        Row(controls=[
                            definition_button('0', expand=2),
                            definition_button('.'),
                            definition_button('='),
                        ]
                        ),   
                ]             
        )
    )
    )

app(target=main)