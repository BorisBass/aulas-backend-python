class BotaoClaro:
    def render(self):
        print("Renderizando botão CLARO")

class BotaoEscuro:
    def render(self):
        print("Renderizando botão ESCURO")


class JanelaClara:
    def render(self):
        print("Renderizando janela CLARA")

class JanelaEscura:
    def render(self):
        print("Renderizando janela ESCURA")


def montar_tela(tema: str):
    # Jeito "natural", com if
    if tema == "claro":
        botao = BotaoClaro()
        janela = JanelaClara()
    else:
        botao = BotaoEscuro()
        janela = JanelaEscura()

    botao.render()
    janela.render()


if __name__ == "__main__":
    tema = input("Digite 'claro' ou 'escuro': ")
    montar_tela(tema)
