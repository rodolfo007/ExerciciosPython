larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg*alt
tinta = area/2

print('A parede tem {}m de largura e {}m de altura, totalizando {}m² \n'
      'Precisará de {}l de tinta para pintar a parede'.format(larg, alt, area, tinta))