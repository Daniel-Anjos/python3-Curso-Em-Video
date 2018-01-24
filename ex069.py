'''Fazer um programa onde o usuário cadastre várias pessoas (idade e sexo) e ao final mostre:
Quantas pessoas maiores de 18
Quantos homens
Quantas mulheres com menos de 20 anos'''

homens = 0
mulheres = 0
maiores = 0
sexo = ' '

while True:
  print('**** Cadastro de Serumaninhos ****')   
  idade = int(input('Informe a idade: '))
  if idade >= 18:
    maiores+= 1
  #while sexo not in ('MF'):
  sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
  if sexo == 'M':
    homens+= 1
  else:
    if idade < 20:
      mulheres+= 1
   
  x = str(input('Deseja cadastrar mais alguém? [S/N]: ')).strip().upper()[0]
  if x == 'N':
    break
    
print(f'''Ao todo você cadastrou: 
         {maiores} pessoas maiores de 18 anos.
         {homens} Homens.
         {mulheres} mulheres com menos de 20 anos. ''')

      
