import textwrap

def menu():
    menu = """\n
    ------------------ MENU --------------
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuario
    [q]\tSair
    =>"""
    return input(textwrap.dedent(menu))
    
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print("\n=== Deposito realizado com sucesso! ===")
    else:
        print("=\n@@@ Operacao falhou! O valor informado e invalido. @@@")
    return saldo, extrato    

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques
    
    if excedeu_saldo:
        print("=\n@@@ Operacao falhou! Acabou o saldo. @@@")
    elif excedeu_limite:
        print("=\n@@@ Operacao falhou! O valor do saque execede o limite. @@@")
    elif excedeu_saques:
        print("=\n@@@ Operacao falhou! Numero maximo de saques excedido. @@@")    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("=\n=== Saque realizado com sucesso! ===")
    else:
        print("=\n@@@ Operacao falhou! Valor informado invalido. @@@")
        
    return saldo, extrato    

def exibir_extrato(saldo, /, *, extrato):
    print("\n ==================Extrato ===================")
    if extrato:
        print(extrato)
    else:
        print("Não foram realizadas movimentações.")
    print("Saldo atual: R$ {:.2f}".format(saldo))

def criar_usuario(usuarios):
    cpf = input("Informe o CPF(somente numero):")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n@@@ Ja existe usuario com este  CPF. Tente novamente.@@@")
        return
    nome = input("Informe nome completo: ")
    data_nascimento = input("Informe a data de nasciomento:")
    endereco = input( "Informe o endereço: ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuario criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios  if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF(somente numero):")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n === Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ usuario nao encontrado, fluxo de criacao de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:\t {conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}"""
        print("=" * 100)
        print(textwrap.dedent(linha))

    
# codigo principal
def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:
        opcao = menu()
    
        if opcao == 'd':
            valor = float(input("Informe o valor do deposito: "))
            if valor > 0:
                saldo, extrato = depositar(saldo, valor, extrato)
            else:
                print("\nValor deve ser maior que zero.")
        
        elif opcao == 's':
            if numero_saques < LIMITE_SAQUES:
                if saldo > 0:
                    saque = float(input("Informe o valor do saque: "))
                    if saque <= limite and saque <= saldo:
                        saldo , extrato = sacar(
                            saldo=saldo,
                            valor=valor,
                            extrato=extrato,
                            limite=limite,
                            numero_saques=numero_saques,
                            limites_saques=LIMITE_SAQUES,
                        )
                    else:
                        print("\nValor de saque invalido. Verifique o limite de R$500.00 e seu saldo disponivel.")
                else:
                    print("\nSaldo insuficiente para realizar saque.")
            else:
                print("\nLimite de saques diarios atingido.")   
        elif opcao == 'e':
            print("\nExtrato:")
            if extrato:
                exibir_extrato(saldo, extrato=extrato)
            else:
                print("Nao foram realizadas movimentacoes.")
            print("Saldo atual: R$ {:.2f}".format(saldo))   
        elif opcao == 'nu':
            criar_usuario(usuarios)
            
        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
        
        elif opcao == 'lc':
            listar_contas(contas)
        
        elif opcao == 'q':
            break
    
        else:
            print("Operacao invalida, por favor selecione novamente a operacao desejada.")

main()