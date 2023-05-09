from flet import app, Container, colors, Row, Column, Page, Text, ElevatedButton, WEB_BROWSER


def main(page: Page) -> None:
    page.title = 'My Calc Flet'
    page.theme_mode = 'dark'
    page.window_width = 300

    result = Text(value='0') 

    def click_action(e) -> None:
        data = e.control.data
        if result.value == "Error" or data == "AC":
            result.value = "0"
            reset()

        elif data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
            result.value += data
            result.update()

    def definition_button(text: str, color: colors=colors.BLACK, 
                        bgcolor: colors=colors.BLUE_GREY_100, expand=1) -> ElevatedButton:
        return ElevatedButton(
            text=text,
            data=text,        
            bgcolor=bgcolor,
            color=color,
            expand=expand,
            on_click=lambda e: click_action(e)
        )
    
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

app(target=main, port=8080, view=WEB_BROWSER)