#sistema bancario_parte 1
#deposito, saque e extrato

#deposito
   #é possível sacar valores positivos e inteiros, apenas.
   #v1 apenas com um usuario
   #os depositos devem ser armazenados em uma variavel e exibidos na operacao de extrato

#saque
    # o sistema deve permitir realizar 3 saques diarios com limite max de 500,00 por saque.
    #caso o usuario nao tenha saldo em conta, o sistema deve exibir uma mensagem informando que nao será possível sacar o dinheiro por falta de saldo.
    #todos os saques devem ser armazenados em uma variavel e exibidos na operacao de extrato.

#extrato
   #listar todos os depositos e saques realizados na conta
   #no fim da listagem deve ser exibido o saldo atual da conta
   #valores devem ser exisibos no formado R$xxx.xx, exemplo 1500,45



from queue import Empty


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

-> """

print(menu)

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu)

    if opcao == "d":
        print("Deposito")
        valor_a_depositar = int(input())
        if(valor_a_depositar >= 1):
            saldo += valor_a_depositar
            #print(f"seu saldo é {saldo}")
            transacao = (f"Depósito no valor de {valor_a_depositar} feito. \n")
            extrato += transacao + "\n"
        else:
            print("não é possível depositar esse valor")

    elif opcao == "s":
        print("Saque")
        numero_saques += 1
        if (numero_saques < 4):
            valor_a_sacar = int(input())
            if (valor_a_sacar <= limite and valor_a_sacar <= saldo):
                saldo -= valor_a_sacar
                transacao = (f"Saque no valor de {valor_a_sacar} feito. \n")
                extrato += transacao + "\n"
                print(f"voce ainda tem direito de sacar mais vezes.")
            elif valor_a_sacar >= limite:
                print("O valor máximo de limite diário é R$500,00 por saque")
            elif valor_a_sacar >= saldo:
                print("Não é possível sacar o dinheiro por falta de saldo")
        else:
            ("Você atingiu o número de saques diário!")
        
    elif opcao == "e":
        print("Extrato")
        if extrato == "":
            print("Não foram realizadas movimentações")
        else:
            print(extrato)
            print(f"Saldo total da conta R$ {saldo:.2f}")

    elif opcao == "q":
        break
    
    else:
        print("Operação inválida. Selecione novamente a operação desejada.")