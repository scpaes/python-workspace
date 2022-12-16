from pibem_bank_system.conta_bancaria import ContaBancaria

if __name__ == "__main__":
    while True:
        print("Selecione a operação \n 1) abrir conta")
        operacao_selecionada = input("")

        match operacao_selecionada:
            case "1":
                dados_para_abertura_conta = input("Informe os dados para abertura da conta: \n nome completo, idade, saldo \n")
                nome_completo, idade, saldo = dados_para_abertura_conta.split(',')
                nova_conta = ContaBancaria.abrir_conta(nome_completo, idade, float(saldo))
                isinstance(nova_conta, ContaBancaria)
