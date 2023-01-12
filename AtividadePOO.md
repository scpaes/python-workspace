PIBEM-BANK SYSTEM

Vamos desenvolver um sistema de banco para os membros da igreja pibem, nesse sistema será necessário realizar o cadastro de contas para os membros da igreja, realizarem transações.

##  Criação de contas:
Para o desenvolvimento da funcionalidade de criação de contas será necessário realizar os seguintes passos.
- Criar uma classe abstrata chamada ContaBancaria.
- Criar classes para os tipos de conta [corrente, salário, poupança], que devem herdar da classe "mãe" ContaBancaria.
- Criar um método(comportamento) para a abertura e para o fechamento de uma conta.

### Propriedades de uma conta: 
- Uma conta deve possuir um saldo, que deve ser do tipo float e não seja negativo
- Deve possuir um cliente atrelado, que deve ser do tipo Cliente.
- Deve possuir um método __str__ para ser representada em texto.
- Uma conta deve possuir um status que pode ser "aberta" ou "fechada"
- Uma conta deve possuir um comportamento de abertura.
- Uma conta deve possuir um comportamento de fechamento.

## Realizar transações:
Para a realização de transações será necessário seguir os seguintes passos.
- Criar uma classe para Operações Bancárias, esta classe deve ser abstrata. 
- Criar um método para realizar depósitos, para realizar um depósito será necessário informar o valor do déposito e a conta de destino.
- Criar um método para realizar transferência, para realizar uma transferência será necessário informar o valor a ser transferido, a conta de origem e a conta de destino.
- Criar um método para realizar saques, para realizar um saque será necessário informar o valor e conta de origem.

### Para cada uma das operações deve haver um método. Para cada operação deve ser necessário a passagem de diferentes argumentos.
