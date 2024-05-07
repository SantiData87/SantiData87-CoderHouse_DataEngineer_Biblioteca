#1--------------------------------------------------------------------------------------------------------------------------------------------------
#Escribir un programa que lea un número impar por teclado. 
#Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.

while True:
    if int(input('Introduce un numero impar:'))% 2==0:
        print('Incorrecto introduce un numero impar') 
    else:
        print('Correcto! Ciclo finalizado')
        break

# La expresión % 2 == 0 se utiliza comúnmente para verificar si un número es par. Esto se debe a que cuando divides un número por 2, 
#si el resto es 0, significa que el número es divisible por 2 y, por lo tanto, es par.
#Mientrasa expresión % 2 !d5= 0 se utiliza comúnmente para verificar si un número es par.

#El simbolo % significa "resto de la division"
#El simbolo // significa division pero solo me trae el numero entero (int)
#El simbolo ** significa elevado


#2--------------------------------------------------------------------------------------------------------------------------------------------------
#Escribir un programa que pida al usuario cuántos números quiere introducir. Luego que lea todos los números y realice una media aritmética.
cantidad=int(input('Introduce una cantidad de numeros para sacar la media:'))
lista=[]
for i in range(cantidad):
    a=float(input('Introduce el numero {}:'.format(i+1)))
    lista.append(a)
print('La media de los numeros es:', sum(lista)/len(lista))



#3--------------------------------------------------------------------------------------------------------------------------------------------------
#Utilizando la función range() y la conversión a listas generar las siguientes listas dinámicamente:
#Todos los números del 0 al 10 [0, 1, 2, ..., 10]
list(range(0,11))
#Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
list(range(-10,1))
#Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
list(range(0,21,2))
#Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
list(range(-19,1,2))
#Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
list(range(0,51,5))

#Solucion de la clase 
print(list(range(0,10+1,1)));
print([x for x in range(-10, 1)])
print([x for x in range(0,20+1,1) if x%2==0])
print([x for x in range(-19, -1+1)])
print([x for x in range(0,50+1,1) if x%5==0])


#4--------------------------------------------------------------------------------------------------------------------------------------------------
#Dadas dos listas (las que se quiera crear), generar una tercera con los elementos que estén presentes en AMBAS listas. 
#Retornar esta nueva lista pero sin elementos duplicados.
lista_1 = ["hola",'mundo', 'cruel']
lista_2 = ["hola",'luna', 'cruel']
nueva_lista = []
for element in lista_2:
    if element in lista_1:
        nueva_lista.append(element)
print([*set(nueva_lista)])


#La funcion set solo devuelve los elementos unicos (podria no usala en este caso)
set([1, 2, 3, 4, 4, 5, 5])

#5--------------------------------------------------------------------------------------------------------------------------------------------------
#Escribir un programa que sume todos los números enteros impares desde el 0 hasta el 100
lista_v=[]
for i in range(1,100+1,1):
    if i %2 ==0:
        lista_v.append(0)
    else:
        lista_v.append(i)
print(sum(lista_v))


#6--------------------------------------------------------------------------------------------------------------------------------------------------
#Contar cuantas veces aparece un elemento en una lista

def conteo(lista, elemento):
    contador = 0
    for elemento in lista:
        if (elemento == x):
            contador = contador + 1
    return contador

lista = [8, 6, 8, 10, 8, 20, 10, 8, 8 ,10, 20]
x = 20 #elemento
print('{} aparece {} veces'.format(x, conteo(lista, x)))



#--------------------------------------------------------------------------------------------------------------------------------------------------