"calcula a hipotenusa"
from math import sqrt
ct1 = float(input("Insira o valor do primeiro cateto: "))
ct2 = float(input("Insira o valor do segundo cateto: "))
hp = sqrt(ct1**2 + ct2**2)
print("A hipotenusa dos catetos oposto e adjacente é {}".format(hp))