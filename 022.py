"""programa que recebe um nome completo e mostra:
- nome com todas as letras maiusculas e minusculas
- quantas letras tem no nome completo
- quantas letras tem o primeiro nome
"""


nome = input("Insira o seu nome completo: ")
tamTexto = len(nome) - nome.count(" ")
priN = nome.split()

print("Seu nome com letras minusculas: ", nome.lower())
print("Seu nome maiusculo: ", nome.upper())
print("Há {} letras no seu nome completo.".format(tamTexto))
print("Há {} letras no seu primeiro nome.".format(len(priN[0])))