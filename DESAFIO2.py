# Sistema Bancário Simples
# Conceitos usados: variáveis, while, break, continue, if/elif/else,
# operadores relacionais e lógicos, strings, input() e float().

menu = """
================ MENU ================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0.0
limite = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# O laço mantém o sistema funcionando até o usuário escolher sair
while True:
    opcao = input(menu).lower().strip()

    if opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: "))
        except ValueError:
            print("Operação falhou! Digite um valor numérico válido.")
            continue

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: "))
        except ValueError:
            print("Operação falhou! Digite um valor numérico válido.")
            continue

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
        elif excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print(f"Operação falhou! O limite por saque é de R$ {limite:.2f}.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques diários excedido.")
        else:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
            print("Saque realizado com sucesso!")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(extrato, end="")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("Obrigado por usar nosso sistema. Até logo!")
        break  # interrompe o laço e encerra o programa

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")