saldo = 1250.00

while True:
    print('Olá, seja bem vindo ao sistema bancário!')
    print('Digite o número da operação que deseja realizar:')

    opção = int(input(
        '1 - consultar saldo\n'
        '2 - realizar saque\n'
        '3 - realizar depósito\n'
        '4 - sair do sistema\n'
        'Digite sua opção: '
    ))

    if opção == 1:
        print(f'Você escolheu consultar saldo. Seu saldo atual é: R${saldo:.2f}')
    elif opção == 2:
        print('Você escolheu realizar saque.')
        valor_saque = float(input('Digite o valor que deseja sacar: '))
        if valor_saque <= saldo:
            saldo -= valor_saque
            print(f'Saque realizado com sucesso. Seu novo saldo é: R${saldo:.2f}')
        else:
            print('Saldo insuficiente.')
    elif opção == 3:
        print('Você escolheu realizar depósito.')
        valor_deposito = float(input('Digite o valor que deseja depositar: '))
        saldo += valor_deposito
        print(f'Depósito realizado com sucesso. Seu novo saldo é: R${saldo:.2f}')
    elif opção == 4:
        print('Você escolheu sair do sistema.')
        break
    else:
        print('Opção inválida. Por favor, digite um número válido.')
