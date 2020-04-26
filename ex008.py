v1 = float(input('Digite o valor do metro: '))

km = v1/1000
hm = v1/100
dam = v1/10
cent = v1*10
dec = v1*100
mm = v1*1000

print('O valor em KM é: {}\n'
      'O valor em DAM é: {}\n'
      'O valor em DEC é: {}\n'
      'O valor em Cent é:{}\n'
      'O valor em Dec é:{}\n'
      'O valor em mm é: {}'.format(km, hm, dam, cent, dec, mm))