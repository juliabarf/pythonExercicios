"programa que lê quatro nomes e retorna os nomes em ordem aleatória."
from random import shuffle

n1 = input("Insira o primeiro nome: ")
n2 = input("Insira o segundo nome: ")
n3 = input("Insira o terceiro nome: ")
n4 = input("Insira o quarto nome: ")

nomes = [n1,n2,n3,n4]
shuffle(nomes)

print("\nSequência dos nomes:\nPrimeiro nome: {}\nSegundo nome: {}\nTerceiro nome: {}\nQuarto nome: {}".format(nomes[0], nomes[1], nomes[2], nomes[3]))