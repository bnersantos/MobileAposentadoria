import flet as ft
from flet import *
from flet.core.dropdown import Option



def main(page: ft.Page):
    page.title = "Rotas"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    def calculo_aposentadoria(e):
        try:
            idade = abs(int(input_idade.value))
            categoria = input_categoria.value
            contribuicao = abs(int(input_contribuicao.value))
            salario = float(input_salario.value)
            genero = input_genero.value
            if idade >= 16:
                if categoria == "Por idade" or "Por tempo":
                    if categoria == "idade":
                        # Por idade
                        if genero == "Masc" or "Fem":
                            if genero == "Masc":
                                if idade >= 65 and contribuicao >= 15:
                                    valor_aposentado = 0.6 * salario + ((contribuicao - 15) * 0.02 * salario)
                                    text_result.value = ("Você pode se aposentar!\n"
                                                         f"R$: {valor_aposentado:.2f}")
                                else:
                                    text_result.value = "Você ainda não pode se aposentar!"
                            elif genero == "Fem":
                                if idade >= 62 and contribuicao >= 15:
                                    valor_aposentado = 0.6 * salario + ((contribuicao - 15) * 0.02 * salario)
                                    text_result.value = ("Você pode se aposentar!\n"
                                                         f"R$: {valor_aposentado:.2f}")
                                else:
                                    text_result.value = "Você ainda não pode se aposentar!"
                            else:
                                text_result.value = "Gênero Inválido, selecione um gênero válido!"
                        else:
                            text_result.value = "Selecione um gênero!"
                    elif categoria == "tempo":
                        # Por tempo
                        if genero == "Masc" or "Fem":
                            if genero == "Masc":
                                if idade >= 51 and contribuicao >= 35 and idade > contribuicao:
                                    valor_aposentado = 0.6 * salario + ((contribuicao - 15) * 0.02 * salario)
                                    text_result.value = ("Você pode se aposentar!\n"
                                                         f"R$: {valor_aposentado:.2f}\n")
                                else:
                                    text_result.value = "Você ainda naõ pode se aposentar!"
                            else:
                                if idade >= 46 and contribuicao >= 30 and idade > contribuicao:
                                    valor_aposentado = 0.6 * salario + ((contribuicao - 15) * 0.02 * salario)
                                    text_result.value = ("Você pode se aposentar!\n"
                                                         f"R$: {valor_aposentado:.2f}\n")
                        else:
                            text_result.value = "Selecione um gênero"
                    else:
                        text_result.value = "Categoria Inválida, escolha uma válida!"
                else:
                    text_result.value = "Escolha um categoria válida"
            else:
                text_result.value = "Idade Inválida, para trabalhar de carteira assinada necessita dos 16 anos completos!"
            page.update()
            page.go("/resultado")
        except ValueError:
            text_result.value = ("Preencha corretamente!")
            page.update()
            page.go("/resultado")

    def gerenciar_rotas(e):
        text.color = Colors.WHITE
        text.size = 12
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Menu"), color=Colors.GREEN_800, bgcolor=Colors.ORANGE),
                    ft.Container(
                        ft.Image(src="inss_icon-removebg-preview.png"),
                    ),
                    ft.Container(
                        height=62,
                    ),
                        ft.Column(
                            [
                                text,
                            ],
                            # Alinhamento da coluna dos botões
                            alignment=ft.alignment.center,
                            horizontal_alignment=ft.alignment.center,
                        ),
                    ft.Container(
                        height=150,
                    ),
                    ft.Container(  # Barra de navegação na parte inferior
                        content=ft.Row(
                            controls=[
                                ft.IconButton(
                                    icon=ft.icons.HOUSE,
                                    icon_color=Colors.GREEN_800,
                                    on_click=lambda _: page.go("/"), ),
                                ft.IconButton(
                                    icon=ft.icons.BOOK,
                                    icon_color=Colors.GREEN_800,
                                    on_click=lambda _: page.go("/condicoes"),
                                ),
                                ft.IconButton(
                                    icon=ft.icons.CALCULATE,
                                    icon_color=Colors.GREEN_800,
                                    on_click=lambda _: page.go("/simulacao"),
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        padding=ft.padding.all(10),
                        bgcolor=Colors.ORANGE,
                    )
                ],
            )
        )

        if page.route == "/simulacao":
            page.views.append(
                View(
                    "/simulacao",
                    [
                        AppBar(title=Text("Simulação"), color=Colors.GREEN_800, bgcolor=Colors.ORANGE),
                        input_idade,
                        Divider(),
                        input_contribuicao,
                        Divider(),
                        input_salario,
                        Divider(),
                        input_genero,
                        Divider(),
                        input_categoria,
                        ElevatedButton("Simular", color=Colors.WHITE, bgcolor=Colors.BLUE_800, width=75, height=50, on_click=lambda _e: calculo_aposentadoria(e)),
                        ft.Container(
                            height=37,
                        ),
                        ft.Container(  # Barra de navegação na parte inferior
                            content=ft.Row(
                                controls=[
                                    ft.IconButton(
                                        icon=ft.icons.HOUSE,
                                        icon_color=Colors.GREEN_800,
                                        on_click=lambda _: page.go("/"), ),
                                    ft.IconButton(
                                        icon=ft.icons.BOOK,
                                        icon_color=Colors.GREEN_800,
                                        on_click=lambda _: page.go("/condicoes"),
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.CALCULATE,
                                        icon_color=Colors.GREEN_800,
                                        on_click=lambda _: page.go("/simulacao"),
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            padding=ft.padding.all(10),
                            bgcolor=Colors.ORANGE,
                        )
                    ],
                )
            )
        elif page.route == "/resultado":
            page.views.append(
                View(
                    "/resultado",
                    [
                        AppBar(title=Text("Resultado"), color=Colors.GREEN_800, bgcolor=Colors.ORANGE),
                        text_result,
                        ElevatedButton("Nova Simulação", on_click=lambda _: page.go("/simulacao")),
                        ElevatedButton("Voltar ao Menu", on_click=lambda _: page.go("/")),
                    ],


                )
            )
        elif page.route == "/condicoes":
            page.views.append(
                View(
                    "condicoes",
                    [
                        AppBar(title=Text("Regras"), color=Colors.GREEN_800, bgcolor=Colors.ORANGE),

                        Text("➡️ Para aposentar-se por idade: \n"
                             "- Homens: 65 anos e pelo menos 15 anos de contribuição.\n"
                             "- Mulheres 62 anos e pelo menos 15 anos de contribuição."),
                        Divider(),

                        Text("➡️ Para aposentar-se por tempo de contribuição: \n"
                             "- Homens: 35 anos de contribuição."
                             "- Mulheres: 30 anos de contrubuição."),
                        Divider(),

                        Text("➡️ O cáculo do benefício considera: \n"
                                "- 60% da média salarial + 2% para cada ano extra de contribuição após 15 anos."),
                        ft.Container(
                            height=177,
                        ),
                        ft.Container(  # Barra de navegação na parte inferior
                            content=ft.Row(
                                controls=[
                                    ft.IconButton(
                                        icon=ft.icons.HOUSE,
                                        icon_color=Colors.GREEN_800,
                                        on_click=lambda _: page.go("/"), ),
                                    ft.IconButton(
                                        icon=ft.icons.BOOK,
                                        icon_color=Colors.GREEN_800,
                                        on_click=lambda _: page.go("/condicoes"),
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.CALCULATE,
                                        icon_color=Colors.GREEN_800,
                                        on_click=lambda _: page.go("/simulacao"),
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            padding=ft.padding.all(10),
                            bgcolor=Colors.ORANGE,
                        )
                    ]
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_views = page.views[-1]
        page.go(top_views.route)
    text = ft.Text("O Instituto Nacional do Seguro Social (INSS) é uma autarquia federal brasileira responsável pela administração dos benefícios previdenciários e assistenciais pagos pelo governo.", size=12, color=Colors.WHITE)
    text_result = ft.Text("", size=18, weight="bold", color="red")
    input_idade = ft.TextField(label="Idade: ")
    input_contribuicao = ft.TextField(label="Tempo de Contribuição: ")
    input_salario = ft.TextField(label="Salário Médio: ")
    input_categoria = ft.Dropdown(
        label="Categorias",
        width=page.window.width,
        options=[Option(key="idade", text="Por Idade"), Option(key="tempo", text="Por Tempo")],
    )
    input_genero = ft.Dropdown(
        label="Gênero",
        width=page.window.width,
        options=[Option(key="Masc", text="Masculino"), Option(key="Fem", text="Femenino")],
    )
    page.on_route_change = gerenciar_rotas
    page.on_view_pop = voltar
    page.go(page.route)


ft.app(main)
