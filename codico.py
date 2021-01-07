def validar_idade(idade):
  if idade < 18 :
    print('\nDesculpe, você nâo tem idade para prossegueir,', nome)
    return False
  else: 
    print('\nÒtimo! podemos prosseguir,', nome)
    return True

def escolha_crata():
  print('digite uma das apoçoes abaixo:')
  print('1 - carro\n2 - mota\n3 - carro e moto')

  return int(input())

def calcular_o_preso(escolha):
  valor_carro = 850
  valor_moto = 850

  if escolha == 1:
    return valor_carro
  elif escolha == 2:
    return valor_moto
  else:
    return valor_carro + valor_moto

def desconto(valor):
    return valor - (valor * 0.10)

nome =input('digite seu nome:')
idade =int(input('digite sua idade'))

if validar_idade(idade):
  escolha = escolha_crata()

  print('\nperfeito! vou calcular a valor')
  valor = calcular_o_preso(escolha)

  print('\n'+nome, 'ovalor total é de', valor, 'reais')
  print('mas vou ver com meu gerente se posso dar um descomto...')
  valor = desconto(valor)

  print('\ncom desconto  eu consigo fazer por', valor, 'reais.')

  print('te interessa?\n1 - sim\n2 -nao')
  interesse = int(input())
  if interesse == 1:
       print('\nperfeito! começaremos amanhã!')
  else:
         print('\nTudo bem :(\nMe avise se mudar de ideia.')