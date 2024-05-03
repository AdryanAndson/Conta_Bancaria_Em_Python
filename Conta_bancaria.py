menu = """
(d) Depositar
(s) Sacar
(e) Extrato
(q) Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).strip().lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$"))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("Limite diário de saques atingido.")
        else:
            valor = float(input("Informe o valor do saque: R$"))

            if valor <= 0:
                print("Valor de saque inválido.")
            elif valor > saldo:
                print("Saldo insuficiente para saque.")
            elif valor > limite:
                print(f"Valor máximo de saque é R${limite:.2f}.")
            else:
                saldo -= valor
                extrato += f"Saque: R${valor:.2f}\n"
                numero_saques += 1
                print(f"Saque de R${valor:.2f} realizado com sucesso.")

    elif opcao == "e":
        print("\n--------------- EXTRATO ----------------")
        if extrato:
            print(extrato, end="")
        else:
            print("Nenhuma movimentação registrada.")
        print(f"Saldo atual: R${saldo:.2f}")
        print("----------------------------------------\n")

    elif opcao == "q":
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")
