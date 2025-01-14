"informações sobre a variável"
car = input("Digite algo: ")
print("O tipo primitivo desse valor é: ", type(car))
print("Tem somente espaço?", car.isspace())
print("é um número? ", car.isnumeric())
print("é alfabetico? ", car.isalpha())
print("é alfanumerico? ", car.isalnum())
print("esta em minusculo? ", car.islower())
print("esta em maiusculo? ", car.isupper())