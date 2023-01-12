from pibem_bank_system.conta_bancaria import ContaCorrente, ContaBancaria, ContaPoupanca, ContaSalario
from pibem_bank_system.pessoas import Cliente
from pibem_bank_system.operacao_bancaria import OperacaoBancaria

if __name__ == "__main__":
    while True:
        print("Selecione a operação \n 1) abrir conta \n 2) Realizar transação ATUALIZADO!!")
        operacao_selecionada = input("")

        match operacao_selecionada:
            case "1":
                dados_para_abertura_conta = input("Informe os dados para abertura da conta: \n nome completo, idade, saldo \n")
                nome_completo, idade, saldo = dados_para_abertura_conta.split(',')
                nome_completo = [item.strip() for item in nome_completo]

                print("Informe o tipo da conta \n 1) corrent \n 2) Poupanca \n 3) Salario")
                tipo_de_conta = input("")

                match tipo_de_conta:
                    case "1":
                        nova_conta = ContaCorrente.abrir_conta(nome_completo, idade, float(saldo))
                    case "2":
                        nova_conta = ContaPoupanca.abrir_conta(nome_completo, idade, float(saldo))
                    case "3":
                        nova_conta = ContaSalario.abrir_conta(nome_completo, idade, float(saldo))

                print(f"Número da conta: {nova_conta.id} saldo: {nova_conta.saldo}")
            case "2":
                print("Informe o tipo da transação: \n 1) Saque \n 2) Depósito")
                tipo_de_transacao = input()

                match tipo_de_transacao:
                    case "1":
                        print("Informar o valor, número da conta")
                        dados_para_realizar_o_saque = input().split(",")
                        valor, numero_conta_bancaria = [item.strip() for item in dados_para_realizar_o_saque]
                        resultado, saldo = OperacaoBancaria.sacar(float(valor), numero_conta_bancaria)
                        print(f"Resultado do saque: {resultado} saldo atualizado: {saldo}")

                    case "2":
                        print("Informe o valor, número da conta")
                        dados_para_realizar_o_deposito = input().split(",")
                        valor, numero_conta_bancaria = [item.strip() for item in dados_para_realizar_o_deposito]
                        resultado, saldo = OperacaoBancaria.depositar(float(valor), numero_conta_bancaria)
                        print(f"Resultado do saque: {resultado} saldo atualizado: {saldo}")
