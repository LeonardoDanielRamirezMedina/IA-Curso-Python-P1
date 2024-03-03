#Leonardo Daniel Ramírez Medina
#6E1 - IA
#03/03/24

#se mostrrá el uso de los argumentos kwargs en diccionarios

#-----Uso de kwargs----

def carros(**kwargs):               #se define la funcion y se usa doble asterisco seguido de kwargs para usar argumentos arbitrarios en diccionarios
    for x in kwargs.values():          #se imprimen los valores del diccionario usando values()
        print("Marca de carro: "+x)     #se imrpime el valor en la posicion x del for

carros(marca="Honda", marca2="Mercedes",marca3="Ford",marca4="Audi")        #se llama a la funcion e introducen los argumentos

#-----uso de return------

def operacion(a,b):     #se define la funcion operacion
    return a*b          #regresa el resultado de la operacion

resultado =operacion(4,5)               #para imprimir el valorregresado se guarda el valor de la funcion en una variable
print("\nResultado de la operacion: ",resultado)        #se imprime la variable
