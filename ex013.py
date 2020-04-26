salario = float(input('Qual o salário do funcionário? R$'))
novosal = salario + (salario * 20 / 100)

print('O funcionário que ganhava R${:.2f}, com a aumento de 20%, agora ganha R${:.2f}'.format(salario, novosal))
