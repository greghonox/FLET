from os import environ
import flet as ft


environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"

global control_reference
control_reference = {}

def add_to_control_reference(key, value) -> None:
    global control_reference
    try:
        control_reference[key] = value
    except KeyError as error:
        print(error)

def return_reference() -> control_reference:
    global control_reference
    return control_reference


class FormHelper(ft.UserControl):
    def __init__(self, user_input):
        self.user_input = user_input
        super().__init__()
        
    def build(self) -> ft.TextField:
        return ft.TextField(
            value=self.user_input,
            border_color='transparent',
            height=20,
            text_size=13,
            content_padding=0,
            cursor_color='black',
            cursor_width=1,
            color='black',
            read_only=True,
            on_blur=lambda e: self.save_value(e) 
        )
    
    def save_value(self, e):
        self.controls[0].read_only = True
        self.controls[0].update()
        

class AppTable(ft.UserControl):
    def __init__(self, page: ft.Page) -> None:
        super().__init__()
        self.page = page
        self.size_heart = page.window_width - 100
        
    def app_data_table_instance(self) -> None:
        add_to_control_reference('AppTable', self)
        
    def build(self) -> ft.Container:
        self.app_data_table_instance()
        return ft.Row(
            width=self.size_heart,
            expand=True,
            controls=[
                ft.DataTable(
                    expand=True,
                    border_radius=8,
                    border=ft.border.all(2, '#ebebeb'),
                    horizontal_lines=ft.border.BorderSide(1, '#ebebeb'),
                    columns=[
                        ft.DataColumn(
                                      ft.Text(
                                        'Column One',
                                        size=12,
                                        color='black',
                                        weight='bold'
                                      )
                        ),
                        ft.DataColumn(
                                      ft.Text(
                                        'Column Two',
                                        size=12,
                                        color='black',
                                        weight='bold'
                                      )
                        ),
                        ft.DataColumn(
                                      ft.Text(
                                        'Column Three',
                                        size=12,
                                        color='black',
                                        weight='bold'
                                      )
                        ),
                        ft.DataColumn(
                                      ft.Text(
                                        'Column Four',
                                        size=12,
                                        color='black',
                                      )
                        ),
                    ],
                    rows=[
                        
                    ]
                )
            ]
        )


class BtnInputForm(ft.UserControl):
    def update_text(self, e):
        e.control.content.controls[0].read_only = False
        e.control.content.controls[0].update()
        
    def get_input_data(self, e):
        for key, value in return_reference().items():
            if key == 'AppForm':
                data = ft.DataRow(cells=[])
                for user_input in value.controls[0].content.controls[0].controls[:]:
                    data.cells.append(
                        ft.DataCell(
                            FormHelper(user_input.content.controls[1].value),
                            on_double_tap=lambda e: self.update_text(e)
                        )
                    )
                    user_input.content.controls[1].value  = ''
                    user_input.content.controls[1].update()
                for user_input in value.controls[0].content.controls[1].controls[:]:
                    data.cells.append(
                        ft.DataCell(
                            FormHelper(user_input.content.controls[1].value),
                            on_double_tap=lambda e: self.update_text(e)
                        )
                    )
                    user_input.content.controls[1].value  = ''
                    user_input.content.controls[1].update()
            if key == 'AppTable':
                value.controls[0].controls[0].rows.append(data)
                value.controls[0].controls[0].update()
                            
    def build(self) -> ft.Container:
        return ft.Container(
            content=ft.ElevatedButton(
                width=220,
                height=42,
                on_click=lambda e: self.get_input_data(e),
                bgcolor='#081d33',
                color='white',
                style=ft.ButtonStyle(
                    shape={
                        "": ft.RoundedRectangleBorder(radius=6),
                    },
                    color={
                        "": "white"
                    }
                ),
                content=ft.Row(
                    controls=[
                        ft.Icon(
                            name=ft.icons.ADD_ROUNDED,
                            size=12,
                        ),
                        ft.Text(
                            'Add Input Field to Table',
                            size=11,
                            weight='bold'
                        )
                    ]
                )
            )
        )


class AppForm(ft.UserControl):
    def __init__(self, page: ft.Page) -> None:
        super().__init__()
        self.page = page
        self.size_heart = page.window_width - 100
        
    def app_form_input_instance(self) -> None:
        add_to_control_reference('AppForm', self)
        
    def app_form_input_field(self, name: str, expand:int ):
        return ft.Container(
            expand=expand,
            height=45,
            border_radius=6,            
            bgcolor='#ebebeb',
            content=ft.Column(
                spacing=1,
                controls=[
                    ft.Text(
                        value=name,
                        size=9,
                        color='black',
                        weight='bold'
                    ),
                    ft.TextField(
                        border='transparent',
                        height=20,
                        text_size=13,
                        content_padding=0,
                        cursor_color='black',
                        cursor_width=1,
                        cursor_height=18,
                        color='black'
                    )                    
                ]
            )
        )
        
    def build(self) -> ft.Container:
        self.app_form_input_instance()
        return ft.Container(
            expand=True,
            width=self.size_heart,
            height=190,
            bgcolor='white10',
            border=ft.border.all(1, '#ebebeb'),
            border_radius=8,
            padding=15,
            content=ft.Column(
                    expand=True,
                    controls=[
                        ft.Row(
                            controls=[
                                self.app_form_input_field('Field *', True),
                            ]
                        ),
                        ft.Row(
                            controls=[
                                self.app_form_input_field('Field One*', 3),
                                self.app_form_input_field('Field Two*', 1),
                                self.app_form_input_field('Field Four*', 1),
                            ]
                        ),   
                        ft.Divider(height=2, color='transparent'),
                        ft.Row(
                            width=self.size_heart,
                            alignment=ft.MainAxisAlignment.END,
                            controls=[
                                BtnInputForm()
                            ]
                        )                                         
                    ]
            )
        )


class Header(ft.UserControl):
    def __init__(self, page: ft.Page) -> None:
        super().__init__()
        self.page = page
        self.size_heart = page.window_width - 100

    def app_header_brand(self) -> ft.Container:
        return ft.Container(
            content=ft.Text('Line Indent', size=15)
        )
                
    def app_header_search(self) -> ft.Container:
        return ft.Container(
            width=self.size_heart - 200,
            bgcolor='white10',
            border_radius=6,
            padding=8,
            opacity=0,
            animate_opacity=300,
            content=ft.Row(
                spacing=10,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Icon(
                        name=ft.icons.SEARCH_OFF_ROUNDED,
                        size=17,
                        opacity=.85
                    ),
                    ft.TextField(
                        width=self.size_heart,
                        border_color='transparent',
                        height=20,
                        text_size=14,
                        content_padding=0,
                        cursor_color='white',
                        cursor_width=1,
                        color='white',
                        hint_text='Search',
                        on_change=lambda e: self.filter_data_table(e),
                    )
                ]
            )
        )
        
    def app_header_avatar(self) -> ft.Container:
        return ft.Container(
            content=ft.IconButton(ft.icons.PERSON)
        )
    
    def show_search_bar(self, e) -> None:
        self.controls[0].content.controls[1].opacity = 1 if e.data == 'true' else 0
        self.controls[0].content.controls[1].update()
        if e.data == 'false':
            self.controls[0].content.controls[1].content.controls[1].value = ''
    
    def filter_data_table(self, e):
        for key, value in return_reference().items():
            if key == 'AppTable':
                if len(value.controls[0].controls[0].rows) != 0:
                    for data in value.controls[0].controls[0].rows[:]:
                        data.visible = True if e.data in data.cells[0].content.controls[0].value.lower() else False
                        data.update()
    
    def build(self):
        return ft.Container(
            width=self.size_heart,
            on_hover=lambda e: self.show_search_bar(e),            
            height=60,
            bgcolor='black',
            expand=True,
            border_radius=ft.border_radius.only(topLeft=15, topRight=15),
            padding=ft.padding.only(left=15, right=15),
            content=ft.Row(
                expand=True,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    self.app_header_brand(),
                    self.app_header_search(),
                    self.app_header_avatar()
                ]
            )
        )
    
        
def main(page: ft.Page):
    header = Header(page)
    form = AppForm(page)
    table = AppTable(page)
    content = ft.Column(
        alignment='center',
        controls=[
            header,
            ft.Divider(height=2, color='transparent'),
            form,
            ft.Column(
                scroll='hidden',
                controls=[
                    table
                ]
            )

        ]
    )
        
    page.add(content)
    page.padding = 10
    page.scroll = "always"
    page.window_width = 500
    page.window_height = 400
    page.window_resizable = False
    page.title = 'Cadastro de Produtos'
    page.bgcolor = 'white'
    page.update()
    
if __name__ == '__main__':
    ft.app(target=main)