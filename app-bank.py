from os import environ
from flet import *
from datetime import datetime
from math import pi


environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"

def create_dark_gradient():
    gradient = LinearGradient(
        begin=alignment.top_center,
        end=alignment.bottom_center,
        colors=[
            '#484848',
            '#444444',
            '#3b3b3b',
            
        ]
    )
    return gradient


class ActivityApp(UserControl):
    def __init__(self, entry_form):
        self.form = entry_form
        super().__init__()
        
    def custom_text_field(self, value: str) -> TextField:
        text = TextField(
                    width=self.form.entry_form.width,
                    cursor_color='white',
                    cursor_width=1,
                    color='white',  
        )
        label = Text(
            value=value,
            size=12,
            color='white',
            weight='bold'
        )
        content = Container(
            width=self.form.entry_form.width,
            alignment=alignment.top_center,
            content=Column(
                controls=[
                    label,
                    text,
                ],
            )
                        
        )
        return content
    
    def save(self, e):
        title = self.controls[0].content.controls[0].content.controls[1].value
        email = self.controls[0].content.controls[1].content.controls[1].value
        self.controls[0].content.controls[0].content.controls[1].value = ''
        self.controls[0].content.controls[1].content.controls[1].value = ''
        self.controls[0].content.controls[0].content.controls[1].update()
        self.controls[0].content.controls[1].content.controls[1].update()
        
    def build(self):
        return Container(
            width=self.form.entry_form.width,
            gradient=create_dark_gradient(),
            content=Column(
                    alignment='center',
                    controls=[
                        self.custom_text_field('tipo conta:'),
                        self.custom_text_field('email:'),
                        IconButton(
                            width=self.form.entry_form.width,
                            icon=icons.APP_REGISTRATION_ROUNDED,
                            icon_color='black',
                            on_click=lambda e: self.save(e)
                        ),
                    ]
                )
        )

class ButtonApp(UserControl):
    def __init__(self, entry_form):
        self.entry_form = entry_form
        self.right_entry = 300
        self.btn = FloatingActionButton(
            content=Icon(
                name=icons.ADD,
                size=18,
                color='white',
                animate_rotation=animation.Animation(600, 'easeOutBack'),
            ),
            bottom=0,
            right=0,
            width=42,
            height=42,
            shape=CircleBorder(),
            offset=transform.Offset(-.5, -.5),
            bgcolor='black',
            on_click=lambda e: self.show_hide_entry_form(e)
        )
        super().__init__()
        
    def show_hide_entry_form(self, e):
        self.entry_form.height = self.right_entry if self.entry_form.height == 0 else 0
        self.btn.content.rotate = transform.Rotate(pi / 4 if self.entry_form.height == self.right_entry else 0)
        self.btn.content.update()
        self.entry_form.update()
        
    def build(self):
        return self.btn


class MainContent(UserControl):
    def __init__(self) -> None:
        self.body = Container(
            width=270,
            height=550,
            border_radius=35,
            border=border.all(5, 'black'),
            padding=padding.only(left=15, top=15, right=15, bottom=10),
            clip_behavior=ClipBehavior.HARD_EDGE,
            gradient=LinearGradient(
                begin=alignment.top_center,
                end=alignment.bottom_center,
                colors=[
                    '#f9f9f9',
                    '#f6f6f6',
                    '#f9f9f9',
                    '#f6f6f6'
                ]
            )
        )
        self.main_stack = Stack()
        self.card_row = Row(
            scroll='hidden'
        )
        self.activity_column = Column(
            expand=True, scroll='hidden'
        )
        self.entry_form = Container(
            width=270,
            height=0,
            margin=margin.only(left=-15, right=-15, top=-25, bottom=25),
            bgcolor='black',
            animate=animation.Animation(300, 'decelerate'),
            alignment=alignment.center,
            content=Container(
                content=Column(
                    alignment='center',
                    controls=[
                        ActivityApp(self)
                    ]
                )
            )
        )
        self.generate_card()
        self.generate_activity()
        super().__init__()
        
    def custom_text(self, value, size, color):
        return Text(value=value, size=size, color=color)

    def generate_card(self) -> list:
        place = ["CVS Qualquer coisa", "Nubank", "Apple Store"] * 2
        price = ["R$ 21,90", "R$ 12.00", "R$ 900,01"] * 2
        card = ["Credit Card = 2135", "Debit CArd - 4122", "Debit Card - 90999"] * 2
        transactions = [
            {
                "time": datetime.now().strftime('%d/%m/%Y'),
                "place": place[i],
                "price": price[i],
                "card": card[i]
            }
                for i in range(6)
        ]
        container_list = [
            Container(
                width=200,
                height=220,
                border_radius=15,
                gradient=create_dark_gradient(),
                padding=20,
                content=Column(
                    spacing=4,
                    alignment='spaceBetween',
                    controls=[
                        self.custom_text(transaction['time'], 10, 'whiete54'),
                        self.custom_text(transaction['place'], 13, 'whiete'),
                        Divider(height=80, color='transparent'),
                        self.custom_text(transaction['price'], 20, 'whiete'),
                        self.custom_text(transaction['card'], 9, 'whiete54'),
                    ]
                )
                
            ) for transaction in transactions
        ]
        self.card_row.controls = container_list
    
    def generate_activity(self) -> list:
        label = [f'Q4 consumer 000{x + 1} label' for x in range(3)]
        misc = ['sdt.expense@gmail.com', 'greghono@gmail.com', 'miriantarifa@gmail.com']
        items = [
            Container(
                width=260,
                height=55,
                bgcolor='#ffffff',
                padding=10,
                content=Column(
                    alignment='center',
                    spacing=0,
                    controls=[
                        Text(label[i], color='black', weight='bold', size=11),
                        Text(misc[i], color='#333333', weight='bold', size=8),
                    ]
                )
            )
            for i in range(3)
            for i in range(3)
        ]
        self.activity_column.controls = items
        
    def build(self) -> Container:
        items: list = [
            Column(
                controls=[
                Row(
                    alignment='spaceBetween', # Faz o espacamento horizontal
                    vertical_alignment='center',
                    controls=[
                        Text(
                            'Hello Line', 
                            color='black', 
                            size=20,
                            width='w600'
                        ),
                        Icon(
                            name=icons.MORE_HORIZ_ROUNDED,
                            color='black',
                            rotate=transform.Rotate(pi / 2),
                        )
                    ],
                ),
                Row(
                    controls=[
                        Text(
                            'Todays Transactions',
                            color='black',
                            size=11,
                            weight='bold',
                        )
                    ]
                ),
                Divider(height=5, color='transparent'),
                self.card_row,
                Divider(height=5, color='transparent'),
                Row(
                    controls=[
                        Text(
                            'Recent Activity',
                            color='black',
                            size=15,
                            weight='bold'
                        ),
                        Divider(height=5, color='transparent'),
                    ]
                ),
                self.activity_column                                
                ]
            ),
            self.entry_form 
        ]
        self.main_stack.controls = items
        self.body.content = self.main_stack
        return self.body


def main(page: Page) -> Container:
    main_content = MainContent()
    btn = ButtonApp(main_content.entry_form)
    
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.bgcolor = '#ffffff'
    
    page.add(
        Stack(
            width=270,
            height=550,
            clip_behavior=ClipBehavior.HARD_EDGE,
            controls=[
                main_content,
                btn
            ]
        )
    )
    page.update()

app(target=main)