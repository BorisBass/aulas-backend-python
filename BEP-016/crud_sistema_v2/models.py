"""
Módulo de Modelos (Entidades)
Aplica conceitos de BEP-017, BEP-018, BEP-019: Classes, Encapsulamento
"""

from datetime import date
from typing import Optional
from .exceptions import DadosInvalidosError


class Aluno:
    """
    Classe que representa um Aluno
    Aplica: Classes, Encapsulamento, Validação
    """
    
    def __init__(self, nome: str, idade: Optional[int] = None, 
                 curso: Optional[str] = None, nota: Optional[float] = None,
                 aluno_id: Optional[int] = None, data_cadastro: Optional[str] = None):
        """
        Construtor da classe Aluno
        
        Args:
            nome: Nome completo do aluno (obrigatório)
            idade: Idade do aluno (opcional)
            curso: Curso do aluno (opcional)
            nota: Nota do aluno entre 0 e 10 (opcional)
            aluno_id: ID do aluno no banco (gerado automaticamente)
            data_cadastro: Data de cadastro (gerada automaticamente)
        """
        # Validações usando encapsulamento
        self._validar_nome(nome)
        self._validar_idade(idade)
        self._validar_nota(nota)
        
        # Atributos privados (encapsulamento)
        self._id = aluno_id
        self._nome = nome
        self._idade = idade
        self._curso = curso
        self._nota = nota
        self._data_cadastro = data_cadastro or str(date.today())
    
    # Getters (BEP-019: Encapsulamento)
    @property
    def id(self) -> Optional[int]:
        """Retorna o ID do aluno"""
        return self._id
    
    @property
    def nome(self) -> str:
        """Retorna o nome do aluno"""
        return self._nome
    
    @property
    def idade(self) -> Optional[int]:
        """Retorna a idade do aluno"""
        return self._idade
    
    @property
    def curso(self) -> Optional[str]:
        """Retorna o curso do aluno"""
        return self._curso
    
    @property
    def nota(self) -> Optional[float]:
        """Retorna a nota do aluno"""
        return self._nota
    
    @property
    def data_cadastro(self) -> str:
        """Retorna a data de cadastro"""
        return self._data_cadastro
    
    # Setters com validação (BEP-019: Encapsulamento)
    @nome.setter
    def nome(self, valor: str):
        """Define o nome do aluno com validação"""
        self._validar_nome(valor)
        self._nome = valor
    
    @idade.setter
    def idade(self, valor: Optional[int]):
        """Define a idade do aluno com validação"""
        self._validar_idade(valor)
        self._idade = valor
    
    @nota.setter
    def nota(self, valor: Optional[float]):
        """Define a nota do aluno com validação"""
        self._validar_nota(valor)
        self._nota = valor
    
    # Métodos privados de validação (encapsulamento)
    def _validar_nome(self, nome: str):
        """Valida o nome do aluno"""
        if not nome or not nome.strip():
            raise DadosInvalidosError("nome", motivo="Nome é obrigatório e não pode estar vazio")
    
    def _validar_idade(self, idade: Optional[int]):
        """Valida a idade do aluno"""
        if idade is not None and (idade < 0 or idade > 150):
            raise DadosInvalidosError("idade", idade, "Idade deve estar entre 0 e 150 anos")
    
    def _validar_nota(self, nota: Optional[float]):
        """Valida a nota do aluno"""
        if nota is not None and (nota < 0 or nota > 10):
            raise DadosInvalidosError("nota", nota, "Nota deve estar entre 0 e 10")
    
    # Métodos de instância
    def atualizar(self, nome: Optional[str] = None, idade: Optional[int] = None,
                  curso: Optional[str] = None, nota: Optional[float] = None):
        """
        Atualiza os dados do aluno
        
        Args:
            nome: Novo nome (opcional)
            idade: Nova idade (opcional)
            curso: Novo curso (opcional)
            nota: Nova nota (opcional)
        """
        if nome is not None:
            self.nome = nome
        if idade is not None:
            self.idade = idade
        if curso is not None:
            self._curso = curso
        if nota is not None:
            self.nota = nota
    
    def to_dict(self) -> dict:
        """
        Converte o aluno para dicionário
        
        Returns:
            Dicionário com os dados do aluno
        """
        return {
            'id': self._id,
            'nome': self._nome,
            'idade': self._idade,
            'curso': self._curso,
            'nota': self._nota,
            'data_cadastro': self._data_cadastro
        }
    
    def to_tuple(self) -> tuple:
        """
        Converte o aluno para tupla (para inserção no banco)
        
        Returns:
            Tupla com os dados do aluno
        """
        return (self._nome, self._idade, self._curso, self._nota)
    
    @classmethod
    def from_tuple(cls, dados: tuple) -> 'Aluno':
        """
        Cria um objeto Aluno a partir de uma tupla do banco de dados
        
        Args:
            dados: Tupla (id, nome, idade, curso, nota, data_cadastro)
        
        Returns:
            Instância de Aluno
        """
        aluno_id, nome, idade, curso, nota, data_cadastro = dados
        return cls(
            nome=nome,
            idade=idade,
            curso=curso,
            nota=nota,
            aluno_id=aluno_id,
            data_cadastro=data_cadastro
        )
    
    def __str__(self) -> str:
        """Representação em string do aluno"""
        idade_str = str(self._idade) if self._idade else "N/A"
        curso_str = self._curso if self._curso else "N/A"
        nota_str = f"{self._nota:.1f}" if self._nota else "N/A"
        
        return (f"Aluno(id={self._id}, nome='{self._nome}', "
                f"idade={idade_str}, curso='{curso_str}', nota={nota_str})")
    
    def __repr__(self) -> str:
        """Representação oficial do aluno"""
        return self.__str__()

