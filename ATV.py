import flet as ft 

def main(page:ft.Page):
    page.title = "Sistema de empréstimo da silva"
    padding = 20

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


    titulo = ft.Container(
        content= ft.Text("Sistema de empréstimo da silva", size=35 ),
        bgcolor= ft.Colors.ORANGE_800,
    )

    
    nome = ft.TextField(label="Digite seu nome",width= 250)

#LISTA DE EQUIPAMENTOS PARA EMPRÉSTIMO
    equipamentos = ft.Dropdown(
        label="Selecione equipamento",
        options=[
        ft.DropdownOption(key="Notebook"),
        ft.DropdownOption(key="Projetor"),
        ft.DropdownOption(key="Multímetro"),

        ]
    )

    quantidade = ft.Slider(min=1, max=10, divisions=100, label="{value}", width= 220)

    resultado = ft.Text("")
#FUNÇÃO PERMITIR EMPRÉSTIMO
    def realizar_emprestimo(e):
        if not nome.value or not equipamentos.value or not quantidade.value:
            resultado.value =("Preencha todos os espaços")
        else:
            resultado.value =f"Parabéns {nome.value}, empréstimo de {quantidade.value} {equipamentos.value}(s) realizado!"
        page.update()


    botao_emprestimo = ft.Button(
        content= "Realizar Empréstimo",
        on_click= realizar_emprestimo,

    )














    coluna = ft.Column(
        controls=[
        titulo,
        nome,
        equipamentos,
        quantidade,
        ft.Row(controls= botao_emprestimo,
               alignment= ft.MainAxisAlignment.CENTER),
               resultado
        ],
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
        scroll=ft.ScrollMode.AUTO

    )

    page.add(coluna)

ft.run(main)