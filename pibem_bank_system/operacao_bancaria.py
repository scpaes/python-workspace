from abc import ABC, abstractmethod
from .conta_bancaria import ContaBancaria


class OperacaoBancaria(ABC):
    @classmethod
    def sacar(cls, valor_do_saque: float, numero_conta_bancaria: str) -> tuple[bool, float]:
        conta_bancaria = [
            conta for numero, conta in ContaBancaria.contas_abertas if numero == numero_conta_bancaria][0]
        if conta_bancaria.saldo < valor_do_saque:
            return False, conta_bancaria.saldo
        conta_bancaria.modificar_saldo("-", valor_do_saque)
        return True, conta_bancaria.saldo

    @abstractmethod
    def depositar(cls, valor_do_deposito: float, conta_bancaria: ContaBancaria) -> tuple[bool, float]:
        return conta_bancaria.modificar_saldo('+', valor_do_deposito)

    @abstractmethod
    def transferir(cls, valor_transferencia: float, conta_origem: ContaBancaria, conta_destino: ContaBancaria) -> bool:
        # remover o saldo da conta de origem
        sucesso, _ = conta_origem.modificar_saldo('-', valor_transferencia)

        if sucesso:
            # creditar o valor na conta de destino
            conta_destino.modificar_saldo('+', valor_transferencia)
            return True

        return False
