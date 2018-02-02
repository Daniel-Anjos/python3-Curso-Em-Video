'''Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. 
No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''

total = 0
cont = 0
menor = 0

print('='*30)
print('*** Lojas Guanabara ***')
print('='*30)
while True:
  nome = str(input('Nome do produto: '))
  preco = float(input('Preço: '))
  total += preco
  if menor == 0:
     menor = preco
  if preco < menor:
     menorNome = nome
     menorPreco = preco
  if preco > 1000:
    cont +=1
  x = ' '
  while x not in 'SN':
    x = str(input('Deseja continuar [S/N]? ')).strip().upper()[0] 
  if x == 'N':
    break
print(f'Total da compra: R${total}')
print(f'Temos {cont} produtos que custam mais de 1000 reais!')
print(f'O produto mais barato foi {menorNome} custando {menorPreco}!')
