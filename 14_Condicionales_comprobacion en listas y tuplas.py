#Leonardo Daniel Ramírez Medina
#6E1 - IA
#02/03/24

#En este código se verá como comporbar datos en listas y cuplas por medio de condicionales

estaciones=("primavera","verano","otoño","invierno")    #se declara la tupla con sus elementos
dato = input("Ingrese una estación del año:\t")     #se pide que se ingrese el dato que se comprobará si está en la tupla

if dato in estaciones:                              #condicion que establece: si dato está en la tupla estaciones entonces imprime lo siguiente:
    print(dato," si es una estacion del año")
else:                                               #si el valor de "dato" no está en la tupla estaciones entonces imprime el siguiente mensaje
    print(dato, "no es una estacion del año")