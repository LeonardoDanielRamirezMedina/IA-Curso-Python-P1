#Leonardo Daniel Ramírez Medina
#6E1 - IA
#03/03/24

#----importaciones y funciones lambda
import math         #se imporya la biblioteca math que nos permite hacer operaciones matematicas mas complejas

areaEsfera= lambda radio:round(4*math.pi*radio*radio,3)         #se hace una funcion en una sola linea gracias a lambda, con el parametro "radio"
print("Area de la esfera:",areaEsfera(4))        #se imprime el resultado de la función 