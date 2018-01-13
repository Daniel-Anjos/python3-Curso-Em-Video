# Digite um número e informe se ele é primo, apenas divisível por 1 e por ele mesmo.

n = int(input('Informe um número: '))
x = 0

for cont in range(1, n + 1):
    if n % cont == 0:
        x += 1
        print('\033[31m', end=' ')
    else:
        print('\033[36m', end=' ')
    print('{}'.format(cont), end=' ')

if x == 2:
    print('\n\033[m O número {} é Primo'.format(n))
else:
    print('\n\033[m O número {} foi divisível {} vezes. Ele NÃO é Primo'.format(n, x))
