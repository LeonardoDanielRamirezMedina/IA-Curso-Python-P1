#Leonardo Daniel Ramírez Medina
#6E1 - IA
#02/03/24

#En este codigo se verá como manejar y convertir tuplas

operacion=("Suma: ","Resta: ", "multiplicacion: ", "Division: ",24, 35, 10)           #Se crea la tupla con sus elementos, los cual no se puede modificar
print(operacion)                   #imprimo el contenido de la tupla
print(operacion[5])                #imprimo una posicion especifica
print(operacion[1],operacion[5],"-",operacion[6],"=",operacion[5]-operacion[6]) #se pueden mostrar los datos, asi como realizar operaciones con ellos

convertList= list(operacion)        #se utiliza el método list() para una tupla en una lista
print(convertList)                  #muestro el contenmido de la lista
print(type(convertList))            #con el método type() se muestra el tipo de dato que es convertList

convertTupla= tuple(convertList)    # con el método tuple() se puede convertir una lista en una tupla
print(convertTupla)                 #se muestra el contenido de convertTupla
print(type(convertTupla))           #se muestra el tipo de dato que es convertTupla