num = int(input('Digite um número: '))

n = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número {}'.format(num))
print('A unidade é: {}'.format(n))
print('A dezena é: {}'.format(d))
print('A centena é: {}'.format(c))
print('A milhar é: {}'.format(m))