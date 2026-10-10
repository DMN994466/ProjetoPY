import time

def cal_qua(x, y): #Calculo da quantidade de pedidos vezes o valor do item
    return x * y

comida = 0
quantidadeC = 0
quantidadeB = 0
bebida = 0
total1 = 0
total2 = 0
valor_total = 0

print("Bem-vindo ao Burguersia! A lanchonete mais saborosa da cidade!")
print("Escolha o seu pedido e bom apetite!")
time.sleep(1) #Pausa de 1 segundo para melhor visualização do menu

while True: #Loop até o fim do pedido
    print("\nMenu:")
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
        comida += quantidadeC
        total1 = cal_qua(ham, quantidadeC)
        break
    elif opcao == 2: #Sanduíche
        print("Opção escolhida: Sanduíche - R$ 15,00")
        quantidadeC = int(input("Digite a quantidade desejada: "))
        comida += quantidadeC
        total1 = cal_qua(sand, quantidadeC)
        break
    elif opcao == 3: #Batata Frita
        print("Opção escolhida: Batata Frita - R$ 8,00")
        quantidadeC = int(input("Digite a quantidade desejada: "))
        comida += quantidadeC
        total1 = cal_qua(batata, quantidadeC)
        break
    elif opcao == 4: #Sorvete
        print("Opção escolhida: Sorvete - R$ 6,00")
        quantidadeC = int(input("Digite a quantidade desejada: "))
        comida += quantidadeC
        total1 = cal_qua(sorvete, quantidadeC)
        break
    else:
        print("Opção inválida. Escolha dentre uma das opções ou cancele o pedido")
