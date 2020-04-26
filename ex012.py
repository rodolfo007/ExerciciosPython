preço = float(input('Qual o preço do produto: R$'))
novop = preço - (preço * 5 / 100)

print('O produto que custava R${:.2f}, agora com o desconto de 5%, vai custar R${:.2f}'.format(preço, novop))
