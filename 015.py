"calcula o preço a pagar por um aluguel de carro."
km = float(input("INsira aqui a quantidade de km pecorrida pelo carro: "))
dias = int(input("Insira aqui a quantidade de dias pelos quais ele foi alugado: "))

precoK = km * 0.15
precoD = dias * 60
total = precoK + precoD

print("O preço a pagar pelo aluguel é de {}".format(total))