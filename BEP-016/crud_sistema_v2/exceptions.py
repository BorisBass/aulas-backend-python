"""
Módulo de Exceções Customizadas
Aplica conceitos de BEP-022: Tratamento de Exceções em POO
"""


class ErroSistema(Exception):
    """Exceção base para erros do sistema"""
    def __init__(self, mensagem: str):
        self.mensagem = mensagem
        super().__init__(self.mensagem)
    
    def __str__(self):
        return f"❌ Erro no Sistema: {self.mensagem}"


class AlunoNaoEncontradoError(ErroSistema):
    """Exceção lançada quando aluno não é encontrado"""
    def __init__(self, aluno_id: int = None, nome: str = None):
        if aluno_id:
            mensagem = f"Aluno com ID {aluno_id} não encontrado!"
        elif nome:
            mensagem = f"Aluno '{nome}' não encontrado!"
        else:
            mensagem = "Aluno não encontrado!"
        super().__init__(mensagem)
        self.aluno_id = aluno_id
        self.nome = nome


class DadosInvalidosError(ErroSistema):
    """Exceção lançada quando dados são inválidos"""
    def __init__(self, campo: str, valor=None, motivo: str = None):
        if motivo:
            mensagem = f"Campo '{campo}': {motivo}"
        elif valor is not None:
            mensagem = f"Valor inválido para '{campo}': {valor}"
        else:
            mensagem = f"Campo '{campo}' inválido!"
        super().__init__(mensagem)
        self.campo = campo
        self.valor = valor


class ErroBancoDados(ErroSistema):
    """Exceção lançada quando há erro no banco de dados"""
    def __init__(self, operacao: str, erro_original: Exception = None):
        mensagem = f"Erro ao {operacao} no banco de dados"
        if erro_original:
            mensagem += f": {erro_original}"
        super().__init__(mensagem)
        self.operacao = operacao
        self.erro_original = erro_original

