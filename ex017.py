import math
co = float(input('Digite o valor oposto:'))
ca = float(input('Digite o valor adjacente: '))
hip = math.hypot(co, ca) #calculo da hipotenusa, usando o import.math

'''hip = (co**2 + ca**2) ** (1/2)''' #calculo sem o import

print('A hipotenusa é: {:.2f}'.format(hip))

