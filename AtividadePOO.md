PIBEM-BANK SYSTEM

Vamos desenvolver um sistema de banco para os membros da igreja pibem, nesse sistema será necessário realizar o cadastro de contas  para os nossos usuários, realizar transações.

##  Criação de contas:
Para o desenvolvimento da funcionalidade de criação de contas será necessário realizar os seguintes passos. 
- Criar uma classe abstrata chamada ContaBancaria.
- Criar classes para os diversos tipos de conta, que devem herdar da classe "mãe" ContaBancaria.

### Propriedades de uma conta: 
- Uma conta deve possuir um saldo, que deve ser do tipo float
- deve possuir um cliente atrelado, que deve ser do tipo Cliente.
- deve possuir um método __str__ para ser representada em texto.
- Uma conta deve possuir um status que pode ser "aberta" ou "fechada"
- Uma conta deve possuir um comportamento de fechamento.

## Realizar transações:
Para a realização de transações será necessário seguir os seguintes passos.
- Criar uma classe para Operações Bancárias, esta classe deve ser abstrata. 
- Criar um método para realizar depósitos.
- Criar um método para realizar transferência. 
- Criar um método para realizar saques. 

### Para cada uma das operações deve haver um método. Para cada operação deve ser necessário a passagem de diferentes argumentos. ex: transaferência requer duas contas, conta de origem e conta de destino.
