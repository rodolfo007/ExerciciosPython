km = float(input('Quantos kilômetros percorreu?:'))
dias = int(input('Quantos dias ficou com o carro?: '))

aluguel = (km * 0.15) +(dias * 60)


print('O valor do aluguel cusa: R${:.2f}'.format(aluguel))

