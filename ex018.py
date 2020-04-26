import math
angulo = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O SENO de {:.0f}, vale {:.2f}'. format(angulo, seno))
print('O COSSENO de {:.0f}, vale {:.2f}'.format(angulo, cosseno))
print('A TANGENTE de {:.0f}, vale {:.2f}'.format(angulo, tangente))
