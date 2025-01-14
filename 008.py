"algoritmo que converte metros em milimetros e centimetros"

metro = float(input("Insira o número em metro para ser convertido: "))
cm = metro * 100
mm = metro * 1000

print("{}m convertido para centímetros é {}\n{}m convertido para milimetro é {}".format(metro,cm,metro,mm))