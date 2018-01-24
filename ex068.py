'''Faça um programa que jogue par ou ímpar com o usuário e pare quando este perder
O programa deve também mostrar a quantidade de vitórias consecutivas do jogador.'''

from random import randint
vitorias = 0
user = ' '

print('=-' * 20)
print('Jogo do Par ou Ímpar')
print('=-' * 20)

while True:
    num = int(input('Digite um valor: '))
    while user not in 'PI':
        user = str(input('Par ou Ímpar? [P/I]: ').strip().upper()[0])
    print('-' * 30)
    x = randint(0, 10)
    total = x + num

    if (total % 2 == 0):
        win = 'P'
        y = 'Par'
    else:
        win = 'I'
        y = 'Ímpar'
    if win == user:
        print(f'Você jogou {num} e o computador {x}. O total foi {total} que é {y}')
        print('Você ganhou!')
        print('Vamos jogar novamente... \n')
    else:
        print(f'Você jogou {num} e o computador {x}. O total foi {total} que é {y}')
        print('Você perdeu')
        break
print('='*20)
print(f'**** GAME OVER ***** \n Você teve {vitorias} vitórias seguidas.')
