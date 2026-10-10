import time
def cal_qua(x, y): #Calculo da quantidade de pedidos vezes o valor do item
    return x * y

quantidadeC = 0
quantidadeB = 0
total1 = 0
total2 = 0
valor_total = 0

print("Bem-vindo ao Burguersia! A lanchonete mais saborosa da cidade!")
print("Escolha o seu pedido e bom apetite!")
time.sleep(1) #Pausa de 1 segundo para melhor visualização do menu

while True: #Refazer o pedido caso o usuário queira
    while True: #Loop até o fim do pedido
        print("\nMenu de comidas:")
        print("""
        1. Hambúrguer
        2. Sanduíche
        3. Batata Frita
        4. Sorvete
        """)
        time.sleep(1.5) #Pausa de 1.5 segundos para melhor visualização do menu
        #Variáveis com valores dos itens
        ham = 12.00
        sand = 15.00
        batata = 8.00
        sorvete = 6.00
        opcao = int(input("Digite o número do item que deseja!(0 para sair): "))
        time.sleep(1) #Pausa de 1 segundo para melhor visualização do menu
        if opcao == 0: #Cancelamento do pedido
            break
        elif opcao == 1: #Hambúrguer
            print("Opção escolhida: Hambúrguer - R$ 12,00")
            quantidadeC = int(input("Digite a quantidade desejada: "))
            total1 += cal_qua(ham, quantidadeC)
            break
        elif opcao == 2: #Sanduíche
            print("Opção escolhida: Sanduíche - R$ 15,00")
            quantidadeC = int(input("Digite a quantidade desejada: "))
            total1 += cal_qua(sand, quantidadeC)
            break
        elif opcao == 3: #Batata Frita
            print("Opção escolhida: Batata Frita - R$ 8,00")
            quantidadeC = int(input("Digite a quantidade desejada: "))
            total1 += cal_qua(batata, quantidadeC)
            break
        elif opcao == 4: #Sorvete
            print("Opção escolhida: Sorvete - R$ 6,00")
            quantidadeC = int(input("Digite a quantidade desejada: "))
            total1 += cal_qua(sorvete, quantidadeC)
            break
        else:
            print("Opção inválida. Escolha dentre uma das opções ou cancele o pedido")
    time.sleep(0.5) #Pausa para melhor visualização do menu
    rep = input("Deseja mais algum item? (Sim/Não): ").upper().strip()[0] #Verificação se o usuário deseja mais algum item
    if rep == "N":
        break
    elif rep == "S":
        continue
    else:
        print("Opção inválida. O pedido será finalizado.")
        break

print(f"\n{total1:.2f} reais em comida foram adicionados ao pedido.")
time.sleep(1)
print("Agora vamos para as bebidas!")

while True: #Refazer o pedido caso o usuário queira
    while True: #Loop até o fim do pedido
        print("\nMenu de bebidas:")
        print("""
        1. Refrigerante
        2. Suco
        3. Água
        """)
        time.sleep(1.5) #Pausa de 1.5 segundos para melhor visualização do menu
        #Variáveis com valores dos itens
        refri = 5.00
        suco = 6.00
        agua = 3.00

        opcao = int(input("Digite o número do item que deseja!(0 para sair): "))
        if opcao == 0: #Cancelamento do pedido
            break
        elif opcao == 1: #Refrigerante
            print("Opção escolhida: Refrigerante - R$ 5,00")
            quantidadeB = int(input("Digite a quantidade desejada: "))
            total2 += cal_qua(refri, quantidadeB)
            break
        elif opcao == 2: #Suco
            print("Opção escolhida: Suco - R$ 6,00")
            quantidadeB = int(input("Digite a quantidade desejada: "))
            total2 += cal_qua(suco, quantidadeB)
            break
        elif opcao == 3: #Água
            print("Opção escolhida: Água - R$ 3,00")
            quantidadeB = int(input("Digite a quantidade desejada: "))
            total2 += cal_qua(agua, quantidadeB)
            break
        else:
            print("Opção inválida. Escolha dentre uma das opções ou cancele o pedido")
    time.sleep(0.5) #Pausa para melhor visualização do menu
    rep = input("Deseja mais algum item? (Sim/Não): ").upper().strip()[0]
    if rep == "N":
        break
    elif rep == "S":
        continue
    else:
        print("Opção inválida. O pedido será finalizado.")
        break

valor_total = total1 + total2
print(f"\n{total2:.2f} reais em bebida foram adicionados ao pedido")
time.sleep(1)

print(f"\nO valor total do pedido é: R$ {valor_total:.2f}")
print(f"\nR${total1:.2f} em comida \nR${total2:.2f} em bebida")
time.sleep(0.5)

print("\nObrigado por comprar conosco! Volte sempre!")