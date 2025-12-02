from abc import ABC, abstractmethod

# ===== Produtos abstratos =====

class Botao(ABC):
    @abstractmethod
    def render(self):
        pass


class Janela(ABC):
    @abstractmethod
    def render(self):
        pass


# ===== Produtos concretos (tema claro/escuro) =====

class BotaoClaro(Botao):
    def render(self):
        print("Renderizando botão CLARO")

class BotaoEscuro(Botao):
    def render(self):
        print("Renderizando botão ESCURO")


class JanelaClara(Janela):
    def render(self):
        print("Renderizando janela CLARA")

class JanelaEscura(Janela):
    def render(self):
        print("Renderizando janela ESCURA")


# ===== Fábrica abstrata =====

class GUIFactory(ABC):
    @abstractmethod
    def criar_botao(self) -> Botao:
        pass

    @abstractmethod
    def criar_janela(self) -> Janela:
        pass


# ===== Fábricas concretas =====

class FabricaTemaClaro(GUIFactory):
    def criar_botao(self) -> Botao:
        return BotaoClaro()

    def criar_janela(self) -> Janela:
        return JanelaClara()


class FabricaTemaEscuro(GUIFactory):
    def criar_botao(self) -> Botao:
        return BotaoEscuro()

    def criar_janela(self) -> Janela:
        return JanelaEscura()


# ===== Código cliente =====

def montar_tela(fabrica: GUIFactory):
    # Aqui não tem if de tema
    botao = fabrica.criar_botao()
    janela = fabrica.criar_janela()

    botao.render()
    janela.render()


if __name__ == "__main__":
    tema = input("Digite 'claro' ou 'escuro': ")

    if tema == "claro":
        fabrica = FabricaTemaClaro()
    else:
        fabrica = FabricaTemaEscuro()

    montar_tela(fabrica)
