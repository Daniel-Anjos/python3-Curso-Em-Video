'''Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

valor = int(input('Informe o valor do saque: R$'))
resto = valor
sobra = 0

notas50 = valor // 50
  resto = valor % 50
  sobra = valor - (notas50 * 50)
  notas20 = (sobra // 20)
  resto = sobra % 20
  sobra = sobra - (notas20 * 20)
  notas10 = (sobra //10)
  resto = sobra % 10
  sobra = sobra - (notas10 * 10)
  notas1 = (sobra // 1)
  resto = sobra % 1
  if resto == 0:
    break

print('Você receberá: ')
if notas50 != 0:
   print(f'{notas50:.0f} notas de R$50,00')
if notas20 != 0:
  print(f'{notas20} notas de R$20,00')
if notas10 != 0:
  print(f'{notas10} notas de R$10,00')
if notas1 != 0:
  print(f'{notas1} notas de R$1,00')

