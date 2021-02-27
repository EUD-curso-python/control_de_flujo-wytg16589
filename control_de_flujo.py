
"""Guarde en lista `naturales` los primeros 100 números naturales (desde el 1) 
usando el bucle while
"""
n=1
naturales=[]
while n<=100 :
  naturales.append(n)
  n+=1

"""Guarde en `acumulado` una lista con el siguiente patrón:

['1','1 2','1 2 3','1 2 3 4','1 2 3 4 5',...,'...47 48 49 50']

Hasta el número 50.
"""
rango=list(range(2,51))
a=1
conc='1'
acumulado=list()
acumulado.append(conc)
for a in rango:
  conc= conc+' '+str(a)
  acumulado.append(conc)
  a+=1



"""Guarde en `suma100` el entero de la suma de todos los números entre 1 y 100:
"""

n=1
suma100=0
while n<=100:
  suma100+=n
  n+=1



"""Guarde en `tabla100` un string con los primeros 10 múltiplos del número 134, 
separados por coma, así:

'134,268,...'

"""
ran=list(range(1,11))
tabla100=''
for a in ran:
  if a==1:
    tabla100= str(a*134)
  else:
    tabla100= tabla100+','+str(a*134)
  a+=1
print (tabla100)


"""Guardar en `multiplos3` la cantidad de números que son múltiplos de 3 y 
menores o iguales a 300 en la lista `lista1` que se define a continuación (la lista 
está ordenada).
"""
lista1 = [12, 15, 20, 27, 32, 39, 42, 48, 55, 66, 75, 82, 89, 91, 93, 105, 123, 132, 150, 180, 201, 203, 231, 250, 260, 267, 300, 304, 310, 312, 321, 326]
multiplos3=0
for n in lista1:
  if n<300 and n%3==0:
    multiplos3+=1
  print(n)
print(multiplos3)



"""Guardar en `regresivo50` una lista con la cuenta regresiva desde el número 
50 hasta el 1, así:

[
  '50 49 48 47...',
  '49 48 47 46...',
  ...
  '5 4 3 2 1',
  '4 3 2 1',
  '3 2 1',
  '2 1',
  '1'
]
"""
tam=50
nlis=50
ser=0
regresivo50=list()
while tam>0:
  con=''
  while ser<tam:
    r2=list(range(1,nlis+1))
    if con=='':
      con=str(r2.pop())
    elif len(r2)>0:
      con=con+' '+str(r2.pop())
    nlis-=1
    ser+=1
  regresivo50.append(con)
  tam-=1
  ser=0
  nlis=tam

"""Invierta la siguiente lista usando el bucle for y guarde el resultado en 
`invertido` (sin hacer uso de la función `reversed` ni del método `reverse`)
"""
lista2 = list(range(1, 70, 5))
invertido=list()
for a in lista2:
  invertido.insert(0,a)



"""Guardar en `primos` una lista con todos los números primos desde el 37 al 300
Nota: Un número primo es un número entero que no se puede calcular multiplicando 
otros números enteros.
"""

lprim=list(range(37,300))
primos=list()
for a in lprim:
  num=a
  sdiv=0
  while num>1:
    if a%num==0:
      sdiv+=1
    num-=1
  if sdiv==1:
    primos.append(a)



"""Guardar en `fibonacci` una lista con los primeros 60 términos de la serie de 
Fibonacci.
Nota: En la serie de Fibonacci, los 2 primeros términos son 0 y 1, y a partir 
del segundo cada uno se calcula sumando los dos anteriores términos de la serie.

[0, 1, 1, 2, 3, 5, 8, ...]

"""
fibonacci=[0,1]
tam=len(fibonacci)
while tam<60:
  term=fibonacci[len(fibonacci)-1]+fibonacci[len(fibonacci)-2]
  fibonacci.append(term)
  tam+=1



"""Guardar en `factorial` el factorial de 30
El factorial (símbolo:!) Significa multiplicar todos los números enteros desde
el 1 hasta el número elegido.

Por ejemplo, el factorial de 5 se calcula así:

5! = 5 × 4 × 3 × 2 × 1 = 120
"""

n=list(range(30,0,-1))
factorial=1
while len(n)>0:
  factorial*=n.pop()

"""Guarde en lista `pares` los elementos de la siguiente lista que esten 
presentes en posiciones pares, pero solo hasta la posición 80.
"""

lista3 = [941, 149, 672, 208, 99, 562, 749, 947, 251, 750, 889, 596, 836, 742, 512, 19, 674, 142, 272, 773, 859, 598, 898, 930, 119, 107, 798, 447, 348, 402, 33, 678, 460, 144, 168, 290, 929, 254, 233, 563, 48, 249, 890, 871, 484, 265, 831, 694, 366, 499, 271, 123, 870, 986, 449, 894, 347, 346, 519, 969, 242, 57, 985, 250, 490, 93, 999, 373, 355, 466, 416, 937, 214, 707, 834, 126, 698, 268, 217, 406, 334, 285, 429, 130, 393, 396, 936, 572, 688, 765, 404, 970, 159, 98, 545, 412, 629, 361, 70, 602]

pos=0
pares=list()
while pos<81:
  if pos%2==0:
    pares.append(lista3[pos])
  pos+=1


"""Guarde en lista `cubos` el cubo (potencia elevada a la 3) de los números del 
1 al 100. 
"""

ncub=list(range(1,101))
cubos=list()
for a in ncub:
  val=a**3
  cubos.append(val)



"""Encuentre la suma de la serie 2 +22 + 222 + 2222 + .. hasta sumar 10 términos 
y guardar resultado en variable `suma_2s` 
"""

nu='2'
tam=1
suma_2s=0
while tam<=10:
  reg=int(nu*tam)
  suma_2s+=reg
  tam+=1



"""Guardar en un string llamado `patron` el siguiente patrón llegando a una 
cantidad máxima de asteriscos de 30. 
*
**
***
****
*****
******
*******
********
*********
********
*******
******
*****
****
***
**
*
"""
pat='*'
linea=1
longitud=30
patron=''
while linea<=longitud:
  patron+=pat*linea+'\n'
  linea+=1
while linea>0:
  if linea==1:
    patron+=pat
    linea-=1  
  elif linea>=longitud:
    linea-=1
  else:
    patron+=pat*linea+'\n'
    linea-=1



