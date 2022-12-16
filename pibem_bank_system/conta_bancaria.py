import random
from abc import ABC
from .pessoas import Cliente


def gerador_id_conta() -> str:
    return ''.join((random.choice('12345') for i in range(5)))


class ContaBancaria(ABC):
    @classmethod
    def abrir_conta(cls, nome_completo: str, idade: int, saldo: float):
        cliente = Cliente(nome_completo, idade)
        conta_bancaria = ContaCorrente(cliente, saldo)

        return conta_bancaria

    def __init__(self, cliente: Cliente, saldo: float = 0) -> None:
        self._saldo = saldo
        self.cliente = cliente
        self.id = gerador_id_conta()

    @property
    def saldo(self):
        return self._saldo

    def modificar_saldo(self, operacao: str, valor: float) -> tuple[bool, float]:
        if (operacao == "-") and self._saldo < valor:
            return False, self._saldo
        elif (operacao == "-"):
            self._saldo -= valor
            return True, self._saldo

        self._saldo += valor
        return True, self._saldo


class ContaCorrente(ContaBancaria):
    def __init__(self, cliente: Cliente, saldo: float = 0) -> None:
        super().__init__(cliente, saldo)

    def __str__(self) -> str:
        return f"Conta corrente número: {self.id} com saldo: {self.saldo}"


class ContaPoupanca(ContaBancaria):
    def __init__(self, cliente: Cliente, saldo: float = 0) -> None:
        super().__init__(cliente, saldo)

    def __str__(self) -> str:
        return f"Conta poupança número: {self.id} com saldo: {self.saldo}"


class ContaSalario(ContaBancaria):
    def __init__(self, cliente: Cliente, saldo: float = 0) -> None:
        super().__init__(cliente, saldo)

    def __str__(self) -> str:
        return f"Conta salário número: {self.id} com saldo: {self.saldo}"
