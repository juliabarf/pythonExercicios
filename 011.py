"calcula a a area da parede para retornar a quantidade necessária de tinta para pintar a parede. 1l = 2m"
larg = float(input("Insira aqui a largura da parede: "))
alt = float(input("Insira aqui a altura da parede: "))

area = larg * alt
tinta = area / 2

print("A área da sua parede é {}m e com essa área será necessário {}l de tinta para pintar a parede.".format(area,tinta))