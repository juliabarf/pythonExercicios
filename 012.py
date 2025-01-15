"desconto de 5% do valor fornecido pelo usuario"

preco = float(input("insira aqui o preço do produto: R$"))
desc = (preco * 5)/100
precoF = preco - desc

print("O seu produto de R${} recebeu um desconto de 5% e o preço final dele é {}".format(preco,precoF))