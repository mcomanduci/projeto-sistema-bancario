menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
depositos = []
saques = []


def depositar(valor):
    global saldo
    if valor < 0:
        print("Valor inválido.")
        return
    saldo += valor
    depositos.append(valor)
    print(f"Depósito de R$ {valor:.2f} efetuado com sucesso.")


def sacar(valor):
    global saldo, numero_saques
    if numero_saques < LIMITE_SAQUES:
        if valor > 500:
            print("Valor máximo de saque é de R$ 500,00.")
            return
        if saldo >= valor:
            saldo -= valor
            saques.append(valor)
            print(f"Saque de R$ {valor:.2f} efetuado com sucesso.")
            numero_saques += 1
        else:
            print("Saldo insuficiente.")
    else:
        print("Limite de saques diários atingido.")


def mostrar_extrato():
    extrato = "Depósitos: \n" + "\n".join([f"R$ {dep:.2f}" for dep in depositos])
    extrato += "\nSaques: \n" + "\n".join([f"R$ {saq:.2f}" for saq in saques])
    extrato += f"\nSaldo: R$ {saldo:.2f}"
    print(extrato)


while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor_deposito = float(input("Digite o valor do depósito: "))
        depositar(valor_deposito)

    elif opcao == "s":
        print("Saque")
        valor_saque = float(input("Digite o valor do saque: "))
        sacar(valor_saque)

    elif opcao == "e":
        print("Extrato")
        mostrar_extrato()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
