#Ler vários números até que o valor 999 seja informado. Ao final mostrar a quantidade de valores informados e a soma deles.

cont = 0
num = 0
total = 0 

while True:
  num = int(input('Digite um número: '))
  if num == 999:
    break
  else:
    cont += 1
    total += num

if cont == 1:
   print (f'A soma do único valor informado é {total}')
else: 
   print (f'A soma dos {cont} valores foi {total}')
   
