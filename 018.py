"programa que recebe um ângulo e imprime na tela o valor do seno, cosseno e tangente do ângulo."
from math import cos, sin, tan, radians

ang = float(input("Insira aqui o ângulo: "))
sen = sin(radians(ang))
coss = cos(radians(ang))
tg = tan(radians(ang))

print("O seno do ângulo {} é {:.2f}\nO cosseno do ângulo {} é {:.2f}\nA tangente do ângulo {} é {:.2f}".format(ang, sen, ang, coss, ang, tg))