"programa que lê o quanto de dinheiro tem na carteira e retorna quanto ela tem em dólares"

din = float(input("Insira aqui quanto de dinheiro tem na sua carteira: R$"))
dol = din / 3.27

print("Você tem U${:.2f}".format(dol))