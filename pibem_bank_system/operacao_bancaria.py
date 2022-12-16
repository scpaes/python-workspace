from abc import ABC, abstractmethod
from .conta_bancaria import ContaBancaria


class OperacaoBancaria(ABC):
    @abstractmethod
    def sacar(cls, valor_do_saque: float, conta_bancaria: ContaBancaria) -> tuple[bool, float]:
        if conta_bancaria.saldo < valor_do_saque:
            return False, conta_bancaria.saldo
        conta_bancaria.saldo = conta_bancaria - valor_do_saque
        return True, conta_bancaria.saldo

    @abstractmethod
    def depositar(cls, valor_do_deposito: float, conta_bancaria: ContaBancaria) -> tuple[bool, float]:
        return conta_bancaria.modificar_saldo('+', valor_do_deposito)

    @abstractmethod
    def sacar(cls, valor_do_saque: float, conta_bancaria: ContaBancaria) -> tuple[bool, float]:
        return conta_bancaria.modificar_saldo('-', valor_do_saque)

    @abstractmethod
    def transferir(cls, valor_transferencia: float, conta_origem: ContaBancaria, conta_destino: ContaBancaria) -> bool:
        # remover o saldo da conta de origem
        sucesso, _ = conta_origem.modificar_saldo('-', valor_transferencia)

        if sucesso:
            # creditar o valor na conta de destino
            conta_destino.modificar_saldo('+', valor_transferencia)
            return True

        return False
