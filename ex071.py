'''Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

valor = int(input('Informe o valor do saque: R$'))
resto = valor

while True:
  if resto == 0:
     break
  else:
    notas50 = (valor / 50)
    resto = valor % 50
    notas20 = (resto / 20)
    resto =  resto % 20
    notas1 = resto / 1
    resto = resto % 1
