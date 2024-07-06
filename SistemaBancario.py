menu = """

 [d] Depositar
 [s] Sacar
 [e] Extrato
 [q] Sair

"""
saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITES_SAQUES = 3

while True:


    opcao = input(menu)


    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou o valor é invalido ")    

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))        

        if valor > saldo:
            print("Operação falhou! voce não tem saldo suficiente.")

        elif valor > limite:
            print("Operação falhou! o valor do saque excede o valor do limite.")

        elif numeros_saques >= LIMITES_SAQUES:
            print("Operação falhou! numero maximo de saques excedidos")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numeros_saques += 1

        else:
            print("Operação falhou! o valor informado é invalido")
    
    elif opcao == "e":
        print("\n================Extrado====================")
        print("nao foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================================")

    elif opcao == "q":
        print("quer sair? tchau!d")
        break
    else:
        print("Operação Invalida, digite uma operação válida!!!")    

        

