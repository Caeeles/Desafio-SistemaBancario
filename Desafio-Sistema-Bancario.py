print("""
    #################################
                Bem-vinde
                    ao
        BANCO NACIONAL de GALAWAY
    #################################
""")

menu = """
Selecione a operação desejada:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

#Variaveis fixas
saldo = 0
limite = 500
extrato = """"""
numero_saques = 0
limite_de_saque = 3

#funções de operaçõesd
def depositar():
    global saldo
    global extrato
    print("Depósito")
    while True:
        valor_deposito = input("Informe o valor que deseja Depositar: ")

        if valor_deposito.isdigit():
            valor_deposito = float(valor_deposito)  
            if valor_deposito > 0: 
                print(f'O valor depositado foi de R${valor_deposito:.2f}')
                saldo += valor_deposito
                transacao = f'Depósito ----- R${valor_deposito:.2f}\n'
                extrato += transacao
                return saldo
            else:
                print('O Valor informado é inválido! Por favor, insira um valor positivo.')
        else:
            print('O Valor informado é inválido! Por favor, insira um valor inteiro.')
def exibirExtrato(): 
    global extrato
    global saldo
    print(f"""
### BANCO NACIONAL de GALAWAY ###
          Extrato Bancário
##################################
{extrato}
##################################
O Saldo Atual da conta é de R${saldo}
##################################
Obrigade...
""")
    return
def sacar():
    global saldo
    global extrato
    global limite
    global numero_saques
    global limite_de_saque
    print("Saque")
    while True:
        valor_saque = input("Informe o valor que deseja Sacar: ")
        valor_saque = float(valor_saque)
        if valor_saque > 0:
            if valor_saque <= saldo:
                if valor_saque <= limite and numero_saques < limite_de_saque:
                    saldo -= valor_saque
                    print(f'O valor sacado foi de R${valor_saque:.2f}')
                    transacao = f'Saque ----- R${valor_saque:.2f}\n'
                    extrato += transacao
                    return saldo
                else:
                    print("Limite excedido. Por favor, verifique se há saldo disponivel ou o limite de saques diários não foi atingido.")
            else:
                print("Saldo excedido. Por favor, verifique se há saldo disponivel ou o limite de saques diários não foi atingido.")
        else:
            print('O Valor informado é inválido! Por favor, insira um valor positivo.')

while True:

    opcao = input(menu)

    if opcao == "d":
        depositar()
        

    elif opcao == "s":
        sacar()

    elif opcao == "e":
        exibirExtrato()
        
    
    elif opcao == "q":
        print("Obrigade por utilizar nosso Banco...")
        break

    else:
        print("Opção inválida, por favor selecione novamente a opção desejada!")
