from abc import ABC


class Pessoa(ABC):
    def __init__(self, nome_completo: str, idade: int) -> None:
        self.nome_completo = nome_completo
        self.idade = idade


class Cliente(Pessoa):
    pass


class Funcionario(Pessoa):
    def __init__(self, nome_completo: str, idade: int, cargo: str) -> None:
        super().__init__(nome_completo, idade)
        set.cargo = cargo
