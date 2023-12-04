#Sistema bancário com depósito, saque, e extrato

extrato = []

opcao = -1
saldo = 0
limite = 0

while opcao != 0:

    print(''' 
    ********** Banco Invest **********

    1 - Sacar
    2 - Depositar
    3 - Extrato
    0 - Sair
    ''')

    opcao = int(input('Operação:'))

    while opcao != 1 and 2 and 3 and 0:
        print('Opção inválida')
        opcao = int(input('Operação:'))

    if opcao == 1:
        if limite < 3:
            quantia = float(input("Valor que deseja SACAR: "))

            if quantia>500:
                print("Limite máximo para saque é de R$500,00")

            elif quantia <= 0:
                print("Não é permitido sacar valores negativos")

            elif quantia> saldo:
                print("Saldo insuficiente para realizar saque")
      
            else:
                saldo -= quantia
                operacao = {f"Saque: -{quantia:.2f}"}
                extrato += operacao
                limite +=1
                print(f'Saque de {quantia:.2f} realizado com sucesso. Seu saldo atual: {saldo:.2f}')
        else:
            print('Não é possível realizar mais saques hoje')
    
    elif opcao == 2:
        quantia = float(input("Valor que deseja DEPOSITAR:"))

        if quantia<=0:
            print('Valor do depósito tem que ser maior que 0')

        else:
        
            saldo += quantia
            operacao = {f"Depósito: {quantia:.2f}"}
            extrato += operacao
            print(extrato)
            print(f"Depósito de {quantia:.2f} realizado com sucesso. Saldo atual: {saldo:.2f}")
    
    elif opcao ==3:
        print('Extrato'.center(30,"="))
        if extrato:
            for operacao  in extrato:
                print(operacao)
            print(f'Seu saldo é de : R${saldo:.2f}')
            print('='*30)

        else:
            print('Nenhuma movimentação identificada')
            print('Saldo de R$ 0,00')
            print('='*30)


print('Obrigado por utilizar nosso sistema. Volte sempre :)')

