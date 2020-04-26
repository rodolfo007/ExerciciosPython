import random
n1 = str(input('Digite o nome: '))
n2 = str(input('Digite outro nome: '))
n3 = str(input('Digite mais outro nome: '))
n4 = str(input('Digite o último nome: '))

lista = [n1, n2, n3, n4]
random.shuffle(lista)

print('A ordem para o sorteio é: ')
print(lista)