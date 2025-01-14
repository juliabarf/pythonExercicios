"mostra o dobro, triplo e a raíz quadrada do numero fornecido"
from math import sqrt

num = int(input("Insira um número: "))
dobro = num * 2
triplo = num * 3
raizQ = sqrt(num)

print("O dobro do número {} é {}\nO triplo do número {} é {}\nA raíz quadrada do número {} é {}".format(num,dobro,num,triplo,num,raizQ))