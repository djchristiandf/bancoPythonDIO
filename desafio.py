menu = """
 [d] Depositar
 [s] Sacar
 [e] Extrato
 [q] Sair
 
=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).strip().lower()
    
    if opcao == 'd':
        valor = float(input("Informe o valor do deposito: "))
        if valor > 0:
            saldo += valor
            extrato += "\nDeposito: R$ {:.2f}\n".format(valor)
        else:
            print("\nValor deve ser maior que zero.")
        
    elif opcao == 's':
        if numero_saques < LIMITE_SAQUES:
            if saldo > 0:
                saque = float(input("Informe o valor do saque: "))
                if saque <= limite and saque <= saldo:
                    saldo -= saque
                    extrato += "\nSaque: R$ {:.2f}\n".format(saque)
                    numero_saques += 1
                else:
                    print("\nValor de saque invalido. Verifique o limite de R$500.00 e seu saldo disponivel.")
            else:
                print("\nSaldo insuficiente para realizar saque.")
        else:
            print("\nLimite de saques diarios atingido.")
   
    elif opcao == 'e':
        print("\nExtrato:")
        if extrato:
            print(extrato)
        else:
            print("Nao foram realizadas movimentacoes.")
        print("Saldo atual: R$ {:.2f}".format(saldo))
   
    elif opcao == 'q':
        break
    
    else:
        print("Operacao invalida, por favor selecione novamente a operacao desejada.")
 