nome = str(input('Digite uma frase: ')).strip().lower()

print('A letra "a" aparece {} vezes'.format(nome.count('a')))
print('Aparece a primeira vez na posição {}'.format(nome.find('a')+1))
print('Aparece a última vez na posição {}'.format(nome.rfind('a')+1))

