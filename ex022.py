nome = str(input('Digite o seu nome: ')).strip()

print('Seu nome em letras maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

separa = nome.split()
print('Seus primeiro nome é {}, e tem {} letras'.format(separa[0], len(separa[0])))

