#Leonardo Daniel Ramírez Medina
#6E1 - IA
#02/03/24

#En este código se verá como comporbar datos en listas y cuplas por medio de condicionales

estaciones=("primavera","verano","otoño","invierno")    #se declara la tupla con sus elementos
dato = input("Ingrese una estación del año:\t")     #se pide que se ingrese el dato que se comprobará si está en la tupla

if dato in estaciones:                              #condicion que establece: si dato está en la tupla estaciones entonces imprime lo siguiente:
    print(dato," si es una estacion del año\n")
else:                                               #si el valor de "dato" no está en la tupla estaciones entonces imprime el siguiente mensaje
    print(dato, "no es una estacion del año\n")

#------Uso de varios condicionales if  (cumplen la funcion de los elif)--------

dato2 = input("Ingrese de nuevo una estación del año:\t")          #se pide que se ingrese un tipo de dato tipo string que se guarda en dato2
if dato2 =="primavera":                                 #Si se cumple: dato2 es igual a "primavera" se imprime la siguiente linea
    print(dato2," si es una estacion del año\n")          
if dato2 =="verano":                                    #Si se cumple: dato2 es igual a "verano" se imprime la siguiente linea
    print(dato2," si es una estacion del año\n")
if dato2 =="otoño":                                     #Si se cumple: dato2 es igual a "otoño" se imprime la siguiente linea
    print(dato2," si es una estacion del año\n")
if dato2 =="invierno":                                  #Si se cumple: dato2 es igual a "invierno" se imprime la siguiente linea
    print(dato2," si es una estacion del año\n")
else:
    print("No es una estación del año")