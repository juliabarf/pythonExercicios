"programa que recebe o valor do salário de um funcionário e retorna p valor com um aumento de 15%"

sal = float(input("Insira aqui seu salário: R$"))
aum = (sal * 15)/ 100
salF = sal + aum
print("Seu salário era de R${} e agora é de R${}".format(sal,salF))