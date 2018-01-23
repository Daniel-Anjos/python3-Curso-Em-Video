#Exibir as tabuadas solicitadas até o número informado ser negativo

while True:
   tab = int(input('Quer ver a tabuada de qual valor? '))
   print('-'*20)
   if tab < 0:
     break
   else: 
     for cont in range (1,11):
        print (f'{tab} X {cont}  = {tab * cont}')
     print('-'*20)
   
print ('\n Fim da Tabuada. ')
   

