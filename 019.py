"programa que lê quatro nomes e retorna um nome aletório entre os que foram selecionados."
from random import choice

n1 = input("Insira o primeiro nome: ")
n2 = input("Insira o segundo nome: ")
n3 = input("Insira o terceiro nome: ")
n4 = input("Insira o quarto nome: ")

nomes = [n1,n2,n3,n4]

print("O nome sorteado foi: ",choice(nomes))