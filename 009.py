"exibir a tabuada do numero fornecido pelo usuario"

num = int(input("Insira um número: "))
i = 0
tabuada = []

while(i <= 10):
    tab = i * num
    print("{} x {} = {}".format(i, num,tab))
    i = i + 1
